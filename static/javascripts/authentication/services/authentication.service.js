/**
 * Created by vishwaraj.sodha on 12/5/16.
 */

(function () {
    'use strict';

    angular.module('slotbooking').factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    function Authentication($cookies, $http) {
        var Authentication = {
            register: register,
            login: login,
            logout: logout,
            getAuthenticatedEmployee: getAuthenticatedEmployee,
            setAuthenticatedEmployee: setAuthenticatedEmployee,
            isAuthenticatedEmployee: isAuthenticatedEmployee,
            unauthenticate: unauthenticate
        };
        return Authentication;

        function register(email, password, confirm_password, username, role, vm){
            return $http.post('/api/v1/employees/',{
                username: username,
                password: password,
                confirm_password: confirm_password,
                email: email,
                role: role
            }).then(registerSuccessFn, registerErrorFn);

            function registerSuccessFn(data, status, headers, config){
                vm.registrationErrorMessage = null;
                Authentication.login(username, password);
            }

            function registerErrorFn(data, status, headers, config){

                if(data.data.username){
                    vm.registrationErrorMessage = "This Username already exists";

                    if(data.data.email){
                        if(data.data.email[0]=="This field must be unique."){
                            vm.registrationErrorMessage = "This Username and Email address already exists";
                        }else
                            vm.registrationErrorMessage = "Enter a valid Email address";
                    }
                }

                else if(data.data.email){
                    if(data.data.email[0]=="This field must be unique."){
                        vm.registrationErrorMessage = "This Email address already exists";
                    }else
                        vm.registrationErrorMessage = "Enter a valid Email address";

                }
                else {
                    vm.registrationErrorMessage = null;
                }


                console.error('Registration failure!');
            }
        }

        function login(username, password, vm){
            return $http.post('/api/v1/auth/login/',{
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

           

            function loginSuccessFn(data, status, headers, config){
                //vm.loginErrorMessage = null;
                // login vm maybe not yet defined so error

                Authentication.setAuthenticatedEmployee(data.data);
                window.location = '/';
            }

            
            function loginErrorFn(data, status, headers, config) {
                vm.loginErrorMessage = data.data.message;
                console.error('Login failure!');
            }
        }

        function logout(){
            return $http.post('/api/v1/auth/logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            function logoutSuccessFn(data, status, headers, config){
                Authentication.unauthenticate();
                window.location = '/';
            }

            function logoutErrorFn(data, status, headers, config){
                console.error("Bhai logout has failed");
            }
        }

        function getAuthenticatedEmployee(){
            /* if(!$cookies.authenticatedEmployee)
             return;
             return JSON.parse($cookies.authenticatedEmployee);*/
            if(!$cookies.getObject('authenticatedEmployee'))
                return;
            return $cookies.getObject('authenticatedEmployee');
        }

        function isAuthenticatedEmployee(){
            //return !!$cookies.authenticatedEmployee;
            return !!$cookies.getObject('authenticatedEmployee');
        }

        function setAuthenticatedEmployee(employee){
            $cookies.putObject('authenticatedEmployee',employee);
            //$cookies.authenticatedEmployee = JSON.stringify(employee);
        }

        function unauthenticate(){
            //delete $cookies.authenticatedEmployee;
            $cookies.remove('authenticatedEmployee');
        }

    }

})();
