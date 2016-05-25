/**
 * Created by vishwaraj.sodha on 18/5/16.
 */
(function(){
    'use strict';

    angular
        .module('slotbooking')
        .controller('HomePageController', HomePageController);

    HomePageController.$inject = ['$location', '$scope', 'Authentication', '$filter', 'BookingSystem'];  // remove authentication if not needed

    function HomePageController($location, $scope, Authentication, $filter, BookingSystem){
        var vm = this;

        vm.currentDate = new Date();

        vm.idSelectedConferenceRoom = null;



        var images = [], x = -1;
        images[0] = "http://cdn.home-designing.com/wp-content/uploads/2013/04/Kayak-Startup-Tech-Office-monochrome-conference-room-white-light-and-view-to-orange-glazing.jpg";
        images[1] = "http://orig00.deviantart.net/0563/f/2013/315/4/b/conference_room__1__by_jons3d-d6tyn7n.jpg";
        images[2] = "http://assets.regus.com/images/1382/meetingroom/4_454x340.jpg";
        images[3] = "http://www.hyperspacellc.com/wp-content/uploads/2014/10/hyp_conference-room-view.jpg";


        var myEl = angular.element( document.querySelector( '#img' ) );
;


        vm.startTimer = function () {
            setInterval(vm.displayNextImage, 6000);
        };


        vm.displayPreviousImage = function () {
            x = (x <= 0) ? images.length - 1 : x - 1;
            myEl[0].src = images[x];
        };


        vm.displayNextImage = function () {
            x = (x === images.length - 1) ? 0 : x + 1;
            myEl[0].src = images[x];
        };



        


        vm.selectedDate = new Date(vm.currentDate);
        //$filter('date')(date, yyyy-MM-dd , timezone)
        //vm.selectedDate = $filter('date')(vm.selectedDate, "yyyy-MM-dd");
        $scope.$watch("vm.selectedDate", function handleDataGet(newValue, oldValue){
            console.log("Selected Date: " , newValue);
        });







        var originalSelectedDate = new Date(vm.selectedDate);
        /*originalSelectedDate.setHours(vm.selectedDate.getHours()+5);
         originalSelectedDate.setMinutes(vm.selectedDate.getMinutes()+30);
         */



        //////////////////////////// you have to set the above thing b4 every call to function using it as parameter

/////////////////////////////             the above one is a work around  .. have to find a way to get this issule of md datepicker solved




        vm.minDate = new Date(
            vm.currentDate.getFullYear(),
            vm.currentDate.getMonth(),
            vm.currentDate.getDate());        // make change over here also .. add 5:30 for viewing perfectly in Datepicker

        vm.maxDate = new Date(
            vm.currentDate.getFullYear(),
            vm.currentDate.getMonth() + 2,
            vm.currentDate.getDate());



        // Here id is to set Database ids for each booking.. if not booked then the id remains null
        vm.slotTimings = [
            {
                id:null, startTime: "09", endTime: "10", isCurrentUserOwner: false, booked: false , slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "10", endTime: "11", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "11", endTime: "12", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "12", endTime: "13", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "13", endTime: "14", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "14", endTime: "15", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "15", endTime: "16", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "16", endTime: "17", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            },
            {
                id:null, startTime: "17", endTime: "18", isCurrentUserOwner: false, booked: false, slotOwner: null, buttonText: "Book", buttonClass: "btn btn-primary btn-sm"
            }
        ];

        vm.rooms = [
            {
                id: 1, name: 'Conference Room 1', imageSoure: "http://orig00.deviantart.net/0563/f/2013/315/4/b/conference_room__1__by_jons3d-d6tyn7n.jpg"
            },
            {
                id: 2, name: 'Conference Room 2', imageSoure: "http://assets.regus.com/images/1382/meetingroom/4_454x340.jpg"
            },
            {
                id: 3, name: 'Conference Room 3', imageSoure: "http://www.hyperspacellc.com/wp-content/uploads/2014/10/hyp_conference-room-view.jpg"
            }
        ];


        vm.selectedRoom = null;


        vm.bookFor = function (slot) {

            var start_date = new Date(vm.selectedDate);                       //  did this because if direct assignment then the pointer assigned
            start_date.setHours(+slot.startTime,0,0,0);  // this + sign converts String to Integer

            /*
             start_date.setHours(start_date.getHours()+5);
             start_date.setMinutes(start_date.getMinutes()+30);
             */


            //var start_date= originalSelectedDate;
            //start_date. about time zone offset to UTC + 05:30 = IST
            //start_date = start_date + start_date.getTimezoneOffset();

            var end_date = new Date(vm.selectedDate); // this passes pointer
            end_date.setHours(+slot.endTime,0,0,0);      // we are not applying filter because it convert a Date object to specific format string object

            /*
             end_date.setHours(end_date.getHours()+5);
             end_date.setMinutes(end_date.getMinutes()+30);
             */

            //var end_date = originalSelectedDate;           debugger;


            // var startInt = new Date(start_date+start_date.getTimezoneOffset());

            if(slot.booked){
                if(slot.isCurrentUserOwner){
                    BookingSystem.unbookConferenceRoom(slot, vm);
                }
            }
            else {
                BookingSystem.bookConferenceRoom(start_date, end_date, this.selectedRoom.id, slot, vm);    // doing this new Date() becoz it converts number date object to
            }
        };



        vm.selectRoom = function (room) {
            vm.selectedRoom = room;

            vm.idSelectedConferenceRoom = room.id;

            myEl[0].src = room.imageSoure;


            vm.jsonData = [];//= null;

            originalSelectedDate = new Date(vm.selectedDate);

            originalSelectedDate.setHours(+vm.slotTimings[0].startTime,0,0,0);
            // this ensures that the info will come starting from the minimum slot time..
            // we do this becoz we will fetch in our case 24th May 9 am to 25th may 8am

            //start_date.setHours(+slot.startTime,0,0,0);

            /*
             originalSelectedDate.setHours(originalSelectedDate.getHours()+5);
             originalSelectedDate.setMinutes(originalSelectedDate.getMinutes()+30);
             */

            BookingSystem.getConferenceInformationFor(room.id, originalSelectedDate, vm);

            $scope.$watch("vm.jsonData", function handleDataGet(newValue, oldValue){
                console.log("Data from backend; " , newValue);
            });               // according to this I do get jsonData for get method from backend



        };

    }

})();


