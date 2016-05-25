/**
 * Created by vishwaraj.sodha on 19/5/16.
 */

(function(){
    'use strict';

    angular.module('slotbooking').factory('BookingSystem', BookingSystem);

    BookingSystem.$inject = ['$http', 'Authentication', '$cookies'];        // later add '$cookies if needed'

    function BookingSystem($http, Authentication, $cookies){
        var BookingSystem = {
            bookConferenceRoom: bookConferenceRoom,
            getConferenceInformationFor: getConferenceInformationFor,
            unbookConferenceRoom: unbookConferenceRoom

        };
        return BookingSystem;



        function getConferenceInformationFor(room_num, selected_date, vm){
            return $http({
                url: '/api/v1/book/',
                method: "GET",
                params: {
                    room_number: room_num,                     // see if name is problematic
                    selected_date: selected_date
                }
            }).then(getConferenceInformationSuccess, getConferenceInformationFailure);


            function getConferenceInformationSuccess(data, status, headers, config){

                vm.jsonData = data.data;


                // disable all before setting any values of new get call

                for (var i=0;i<vm.slotTimings.length;i++) {
                    vm.slotTimings[i].id = null;
                    vm.slotTimings[i].booked = false;
                    vm.slotTimings[i].slotOwner = null;
                    vm.slotTimings[i].isCurrentUserOwner = false;
                    vm.slotTimings[i].buttonText = "Book";
                    vm.slotTimings[i].buttonClass= "btn btn-primary btn-sm";
                }
                // able it after disable only



                for (i=0; i < vm.slotTimings.length ; i++) {
                    for(var j=0; j < vm.jsonData.length ; j++){
                        var dateObject = new Date(vm.jsonData[j].start_date);
                        
                        /*
                        dateObject.setHours(dateObject.getHours()-5);
                        dateObject.setMinutes(dateObject.getMinutes()-30);
                        */
                        
                        var hoursObject = dateObject.getHours();
                        //if(parseInt(String(hoursObject)) == parseInt(vm.slotTimings[i].startTime)){}
                        if(parseInt(hoursObject) == parseInt(vm.slotTimings[i].startTime)){
                            // entering this condition means that the slot is booked

                            vm.slotTimings[i].id = vm.jsonData[j].id; // this id means the id of booking .. where for a particular day , particular room , particular slot.. but we give id temporarily to a slot then flush it
                            vm.slotTimings[i].booked = true;
                            vm.slotTimings[i].slotOwner = vm.jsonData[j].booker_of_slot;
                            //vm.slotTimings[i].buttonClass= "btn btn-primary";


                            var currentUser = Authentication.getAuthenticatedEmployee();

                            if(currentUser.id == vm.jsonData[j].booker_of_slot.id){
                                //entering this condition means that slot is owned by current user

                                vm.slotTimings[i].isCurrentUserOwner = true;
                                vm.slotTimings[i].buttonText = "Unbook";
                                vm.slotTimings[i].buttonClass= "btn btn-danger btn-sm";

                            }
                            else {
                                vm.slotTimings[i].buttonText = "Booked";
                                vm.slotTimings[i].buttonClass= "btn btn-primary btn-sm disabled";
                            }
                            break;
                        }
                    }

                }

                /// once set give buttons a specific class according to their state


            }

            function getConferenceInformationFailure(data, status, headers, config){}

        }




        function bookConferenceRoom(start_date, end_date, room_booked, slot, vm){

            debugger;
            return $http({
                url: '/api/v1/book/',
                method: "POST",
                data: {
                    start_date: start_date,
                    end_date: end_date,
                    room_booked: room_booked
                }


            }).then(bookingSuccess,bookingFailure);


            function bookingSuccess(data, status, headers, config){

                slot.id = data.data.id;
                slot.booked = true;
                slot.slotOwner = Authentication.getAuthenticatedEmployee();
                slot.isCurrentUserOwner = true;
                slot.buttonText = "Unbook";
                slot.buttonClass= "btn btn-danger btn-sm";

            }

            function bookingFailure(data, status, headers, config){
                // put some alert code for failure of booking
            }


        }



        function unbookConferenceRoom(slot, vm){
            return $http({
                url: '/api/v1/book/'+slot.id+'/',
                method: "DELETE"

            }).then(unbookSuccess, unbookFailure);

            function unbookSuccess(data, status, headers, config){
                // code for unbook Success

                slot.id = null;
                slot.booked = false;
                slot.slotOwner = null;
                slot.isCurrentUserOwner = false;
                slot.buttonText = "Book";
                slot.buttonClass= "btn btn-primary btn-sm";

            }

            function unbookFailure(data, status, headers, config){


            }



        }


    }

})();
