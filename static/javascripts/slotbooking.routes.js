/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking.routes').config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider){
        $routeProvider.when('/register',{
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/register.html'
        }).otherwise('/');
    }
})();