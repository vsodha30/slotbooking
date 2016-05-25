/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking').config(config);

    config.$inject = ['$routeProvider'];

    /*function config($routeProvider){
     $routeProvider.when('#/register',{
     controller: 'RegisterController',
     controllerAs: 'vm',
     templateUrl: '/static/templates/authentication/register.html'
     }).otherwise('/');
     }
     })();*/

    function config($routeProvider) {
        $routeProvider/*.when('/', {
         controller: 'IndexController',
         controllerAs: 'vm',
         templateUrl: '/static/templates/layout/index.html'
         })*/
            .when('/homepage', {
                controller: 'HomePageController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/bookingsystem/homepage.html'
            })
            .when('/register', {
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
                //templateUrl: '/templates/register.html'
            })
            .when('/login', {
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .otherwise('/login');
    }
})();