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
.controller 'CarCtrl', ($scope, $routeParams, $http, $log, $interval) ->

    $scope.moveStatus = {
        forward: false
        backward: false
        left: false
        right: false
    }

    # TODO
    carId = $routeParams.id
    $scope.car = {
        name: 'Марк 1',
#        address: '192.168.150.109',
        address: '10.0.1.4',
#        address: '127.0.0.1',
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
        url = "http://#{$scope.car.address}:4242/command/"
        params = {name: commandName}
        $http.post(url, $.param(params))

