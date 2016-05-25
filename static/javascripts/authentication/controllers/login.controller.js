/**
 * Created by vishwaraj.sodha on 16/5/16.
 */

(function () {
  'use strict';

  angular
    .module('slotbooking')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$location', '$scope', 'Authentication'];

  function LoginController($location, $scope, Authentication) {
    var vm = this;

    vm.login = login;
    
    vm.loginErrorMessage = null;

    activate();

    function activate() {
      // If the employee is authenticated, then the employee should be redirected to home page .
      if (Authentication.isAuthenticatedEmployee()) {
        //$location.url('/api/v1/employees/');
      }
    }

    function login() {
      Authentication.login(vm.username, vm.password, vm);
    }
  }
})();