		// This is a expanded version of javascript code
		// var username = document.getElementById("c-username");
		// var usernameHelp = document.getElementById("usernameHelp");
		// var accountCreateBtn= document.getElementsByClassName("ac-create")[0];
		// username.onkeyup = function() {
		// 	var _username = this.value; 
		// 	if(_username.length > 0 && _username.length < 21) {
		// 		$.ajax({
		// 			type:"GET",
		// 			url:"{% url 'user:usernameExist' %}",
		// 			data:{
		// 				'_username':_username
		// 			},
		// 			success:function(json) {
		// 				username_regex=/[!@#$%^&*:;,.?]/;
		// 				if(json.successfull) {
		// 					if(_username.split(" ").length == 1) { 
		// 						//There should be no space and is a valid username
		// 						if(!_username.match(username_regex)) {
		// 							//No special characters and is VALID
		// 							if(json.can_be_taken) {
		// 								//username is unique
		// 								usernameHelp.innerHTML="<span class='text-success'>Username can be taken</span>";
		// 			                	username.style.borderColor = 'green';
		// 								username.style.boxShadow = '0 0 4px lightgreen';
		// 								//ONLY HERE THE USERNAME IS COMPLETELY VALID
		// 								accountCreateBtn.removeAttribute('disabled');
		// 							}
		// 							else {
		// 								//username is not unique
		// 								usernameHelp.innerHTML="<span class='text-danger'>Username is already taken</span>";
		// 			               	 	username.style.borderColor = 'red';
		// 								username.style.boxShadow = '0 0 2px red';
		// 								accountCreateBtn.setAttribute('disabled',true);
		// 							}
		// 						}
		// 						else {
		// 							//Special characters are there
		// 							usernameHelp.innerHTML="<span class='text-danger'>There can be no Special Characters</span>";
		// 			                username.style.borderColor = 'red';
		// 							username.style.boxShadow = '0 0 2px red';
		// 							accountCreateBtn.setAttribute('disabled',true);
		// 						}
		// 					}
		// 					else {
		// 						//invalid exceeding one word
		// 		                usernameHelp.innerHTML="<span class='text-danger'>There should be no whitespace between username</span>";
		// 		                username.style.borderColor = 'red';
		// 						username.style.boxShadow = '0 0 2px red';
		// 						accountCreateBtn.setAttribute('disabled',true);
		// 					}
		// 				}
		// 				else {
		// 					alert("Something went wrong");
		// 				}
		// 			}
		// 		});
		// 	}
		// 	else if(_username.length >= 21){
		// 		usernameHelp.innerHTML = "<span class='text-danger'>Username can't be more than 20 characters</span>"
		// 		this.style.borderColor = 'red';
		// 		this.style.boxShadow = '0 0 2px red';
		// 	}
		// 	else {
		// 		usernameHelp.innerHTML = "<span class='text-muted'>Username can't be left empty</span>"
		// 		this.style.borderColor = 'grey';
		// 		this.style.boxShadow = '0 0 2px grey';
		// 	}
		// }