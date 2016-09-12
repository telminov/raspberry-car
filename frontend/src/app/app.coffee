angular.module('RPiCar', [
    'ngResource'
    'ngSanitize'
    'ngRoute'
    'ngAnimate'
    'ngStorage',

    'ui.bootstrap'

    'swUtils'
])


.config ($routeProvider) ->
    $routeProvider
        .when('/',
          templateUrl: 'controllers/main.html'
          controller: 'MainCtrl'
          label: ''
        )
        .when('/current/',
          templateUrl: 'controllers/car.html'
          controller: 'CarCtrl'
          label: 'Current Car'
        )


.run ($location, $rootScope, swTitle) ->
    $rootScope.swTitle = swTitle
    $rootScope.$on '$routeChangeSuccess', (event, current, previous) ->
        baseTitle = current.$$route?.label or ''
        swTitle.setTitleBase(baseTitle)
        swTitle.setTitleStart('')
        swTitle.setTitleEnd('')


.config ($httpProvider) ->
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'