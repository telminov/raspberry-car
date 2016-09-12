SPACE_KEY_CODE = 32

FORWARD_KEY_CODE = 38
BACKWARD_KEY_CODE = 40
LEFT_KEY_CODE = 37
RIGHT_KEY_CODE = 39

BTN_DIRECTIONS = {
    forwardBtn: 'forward'
    backwardBtn: 'backward'
    leftBtn: 'left'
    rightBtn: 'right'
}

angular.module('RPiCar')
.controller 'CarCtrl', ($scope, $routeParams, $http, $log, $interval, $localStorage, $location, car) ->
    # если нет некущей тачки
    if not car.getCurrentCar()
        $location.path('/')

    $scope.car = car.getCurrentCar()
    $scope.speed = $localStorage.speed or 100
    $scope.setSpeed = (value) ->
        $localStorage.speed = value
        $scope.speed = value

    $scope.moveStatus = {
        forward: false
        backward: false
        left: false
        right: false
    }


    $scope.commandLog = []
    $scope.carCommandHandler = (commandResponse) ->
        item = {
            response: JSON.parse(commandResponse)
            dt: new Date()
        }
        $scope.commandLog.unshift(item)

        if $scope.commandLog.length > 5
            $scope.commandLog.length = 5



    $scope.move = (direction, state) ->
        oldState = $scope.moveStatus[direction]
        $scope.moveStatus[direction] = state
        if oldState != state
#            sendMoveStatus($scope.moveStatus)
            sendMoveStatus(direction, state)


    $scope.keyDownHandler = (event) ->
        direction = _getDirection(event)
        if direction
            $scope.move(direction, true)

    $scope.keyUpHandler = (event) ->
        direction = _getDirection(event)
        if direction
            $scope.move(direction, false)


    _getDirection = (event) ->
        if event.keyCode == SPACE_KEY_CODE and event.target.type == 'button'
            direction = BTN_DIRECTIONS[event.target.id]
            return direction

        if event.keyCode == FORWARD_KEY_CODE
            return 'forward'

        if event.keyCode == BACKWARD_KEY_CODE
            return 'reverse'

        if event.keyCode == LEFT_KEY_CODE
            return 'left'

        if event.keyCode == RIGHT_KEY_CODE
            return 'right'

        return undefined

    currentIntervals = {}
    sendMoveStatus = (direction, state) ->
#        data = JSON.stringify(moveStatus)
        console.debug(direction, state)

        if state
            sendCommand(direction)
            cancelInterval(direction)   # на всякий случай
            currentIntervals[direction] = $interval(
                ->
                    sendCommand(direction)
                300
            )
        else
            cancelInterval(direction)

            if direction == 'forward' or direction == 'reverse'
                sendCommand('stop')
            else if direction == 'left' or direction == 'right'
                sendCommand('center')

    cancelInterval = (name) ->
        if currentIntervals[name]
            $interval.cancel(currentIntervals[name])
            delete currentIntervals[name]


    sendCommand = (commandName) ->
        console.debug(commandName)

        value = ''
        if commandName == 'forward' or commandName == 'reverse'
            value = $scope.speed

        url = "#{$scope.car.url}command/"
        params = {name: commandName, value: value}
        $http.post(url, $.param(params))

