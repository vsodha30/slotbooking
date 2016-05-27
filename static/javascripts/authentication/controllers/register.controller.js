/**
 * Created by vishwaraj.sodha on 12/5/16.
 */
(function () {
    'use strict';

    angular.module('slotbooking').controller('RegisterController',RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    function RegisterController($location, $scope, Authentication) {
        var vm = this;

        vm.register = register;

        vm.registrationErrorMessage = null;

/*        vm.formData ={ 
            password_c:''
    };*/


        /*activate();

         function activate() {
         // If the employee is authenticated, then the employee should be redirected to home page .
         if (Authentication.isAuthenticatedEmployee()) {
         $location.url('/api/v1/employees/');
         }
         }*/



        // keep checks and validation for role , email , username
        // add confirm password feature



        vm.data = {
            selectedRole: null,
            availableRoles: [
                {id: 'CEO', name: 'CEO'},
                {id: 'Manager', name: 'Manager'},
                {id: 'Project Lead', name: 'Project Lead'},
                {id: 'Software Developer', name: 'Software Developer'},
                {id: 'Junior Software Developer', name: 'Junior Software Developer'},
                {id: 'HR Manager', name: 'HR Manager'},
                {id: 'Quality Assurance Engineer', name: 'Quality Assurance Engineer'}
            ]
        };


        function register() {
            Authentication.register(vm.email, vm.password, vm.confirm_password, vm.username, vm.data.selectedRole, vm)
        }


    }
})();