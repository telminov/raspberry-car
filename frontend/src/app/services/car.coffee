angular.module('RPiCar')
.service 'car', ($localStorage) ->

    this.setCurrentCar = (car) ->
        $localStorage.currentCar = car

    this.getCurrentCar = ->
        return $localStorage.currentCar

    return
