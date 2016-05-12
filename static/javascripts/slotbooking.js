/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking', ['slotbooking.routes', 'slotbooking.authentication']);
    
    angular.module('slotbooking.routes', ['ngRoute']);

    angular.module('slotbooking').run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();