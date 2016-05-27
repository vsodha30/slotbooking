/**
 * Created by vishwaraj.sodha on 27/5/16.
 */

(function () {
    angular.module('slotbooking').directive('validPasswordC', function () {
        return {
            require: 'ngModel',
            link: function (scope, element, attributes, ngModelCtrl) {
                ngModelCtrl.$parsers.unshift(function (viewValue, $scope) {
                    var noMatch = viewValue != scope.registrationForm.register__password.$viewValue;
                    ngModelCtrl.$setValidity('noMatch', !noMatch);
                    return (noMatch)?noMatch:!noMatch;
                });
            }
        }
    });
})();



// The below one is generalized when the password is passed as attribute value in this directive .. the password is then compared to confirm password



/*
var app = angular.module('app', []);
app.directive('validPasswordC', function() {
  return {
    require: 'ngModel',
    scope: {

      reference: '=validPasswordC'

    },
    link: function(scope, elm, attrs, ctrl) {
      ctrl.$parsers.unshift(function(viewValue, $scope) {

        var noMatch = viewValue != scope.reference
        ctrl.$setValidity('noMatch', !noMatch);
        return (noMatch)?noMatch:!noMatch;
      });

      scope.$watch("reference", function(value) {;
        ctrl.$setValidity('noMatch', value === ctrl.$viewValue);

      });
    }
  }
});
app.controller('homeCtrl', function($scope) {

});*/
