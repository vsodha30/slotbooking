/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking', ['ngRoute', 'ngCookies', 'ngMaterial']);


    angular.module('slotbooking').run(runBlock);

    runBlock.$inject = ['$http', 'Authentication', '$rootScope', '$location'//, '$cookies', '$rootScope'
    ];

    function runBlock($http, Authentication, $rootScope, $location//, $cookies, $scope
    ) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';

   

        $rootScope.$on("$routeChangeStart", function (event, next, current) {
            if(next.templateUrl === "/static/templates/authentication/register.html"){
            }
            else if(next.templateUrl === "/static/templates/authentication/login.html"){
            }
            else{
                if(!Authentication.isAuthenticatedEmployee()){
                    $location.path('/login');
                }
            }

        });


    }
})();