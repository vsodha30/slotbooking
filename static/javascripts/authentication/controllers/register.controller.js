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

        // keep checks and validation for role , email , username
        // add confirm password feature

        vm.data = {
            selectedRole: null,
            availableRoles: [
                {id: 'C', name: 'CEO'},
                {id: 'M', name: 'Manager'},
                {id: 'P', name: 'Project Lead'},
                {id: 'S', name: 'Software Developer'},
                {id: 'J', name: 'Junior Software Developer'},
                {id: 'H', name: 'HR Manager'},
                {id: 'Q', name: 'Quality Assurance Engineer'}
            ]
        };


        function register() {
            Authentication.register(vm.email, vm.password, vm.username, vm.data.selectedRole)
        }
    }
})();