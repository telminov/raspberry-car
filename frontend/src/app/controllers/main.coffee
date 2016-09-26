angular.module('RPiCar')
.controller 'MainCtrl', ($scope, $log, $localStorage, $http, $location, car) ->
    $scope.cars = []
    $scope.network = $localStorage.network

    $scope.scan = ->
        $scope.cars.length = 0
        $localStorage.network = $scope.network

        for i in [1..254]
            address = "#{ $scope.network }#{ i }"

            url = "http://#{address}:4242/"
            $http.get(url).then(
                (result) ->
                    $scope.cars.push({
                        address: result.data.address
                        url: result.config.url
                        name: result.data.name
                    })
                ->
            )

    if $scope.network
        $scope.scan()

    $scope.openCar = (currentCar) ->
        car.setCurrentCar(currentCar)
        $location.path('/current/')