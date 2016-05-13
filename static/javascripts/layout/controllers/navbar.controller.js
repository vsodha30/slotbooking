/**
 * NavbarController
 * @namespace slotbooking.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('slotbooking')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
   * @namespace NavbarController
   */
  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    /**
     * @name logout
     * @desc Log the user out
     * @memberOf slotbooking.layout.controllers.NavbarController
     */
    function logout() {
      Authentication.logout();
    }
  }
})();
