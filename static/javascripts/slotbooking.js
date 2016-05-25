/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking', ['ngRoute', 'ngCookies', 'ngMaterial']);


    angular.module('slotbooking').run(runBlock);

    runBlock.$inject = ['$http'//, '$cookies', '$rootScope'
    ];

    function runBlock($http//, $cookies, $scope
    ) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();