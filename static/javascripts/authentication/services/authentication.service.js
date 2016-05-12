/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';
    
    angular.module('slotbooking.authentication.services').factory('Authentication', Authentication);
    
    Authentication.$inject = ['$cookies', '$http'];
    
    function Authentication($cookies, $http) {
        var Authentication = {
          register: register  
        };
        return Authentication;

        function register(email, password, username){
            return $http.post('/api/v1/employees/',{
                username: username,
                password: password,
                email: email
            });
        }

    }
    

})();
