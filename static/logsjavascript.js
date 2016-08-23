var tableData = '<table id="tableID"><tr><th>Campus</th><th>Building</th><th>Room Number</th><th>Day</th><th>Date</th><th>Time</th><th>Year</th><th>Associated credit count</th><th>Authenticated credit count</th><th>Average Users</th></tr>';

	function AllData(){
		
 		var c = document.getElementById("classroom").value;
 		var path = "/json1/"+c;
 		var new_date = [];
		var users = [];	
    	var j={};  
    
    	var btn1 = document.createElement("BUTTON");
		document.body.appendChild(btn1);
		btn1.setAttribute('type','button');
		btn1.setAttribute('class', 'prevbtn');
		btn1.setAttribute('id','previous');
		btn1.innerHTML = 'previous';
		btn1.style.position = "absolute";
		btn1.style.left = "80px";
		btn1.style.top = "625px";
		btn1.style.height = "30px";
		btn1.style.width = "80px";
		
		
		
    	var btn = document.createElement("BUTTON");
		document.body.appendChild(btn);
		btn.setAttribute('type','button');
		btn.setAttribute('class', 'nextbtn');
		btn.setAttribute('id','next');
		btn.innerHTML = 'next';
		btn.style.position = "absolute";
		btn.style.left = "175px";
		btn.style.top = "625px";
		btn.style.height = "30px";
		btn.style.width = "80px";
		
    	
 		d3.json(path,function(data){
 			$.each(data, function(index, new_data){
 					dates = new Date(new_data[0]);
        		   new_date.push(dates/1000);
        		   users.push(parseInt(new_data[1]));
        	   });
 			
 			for (i=0; i<new_date.length;i++){
// 				alert(new_date[i]);
// 				alert(users[i]);
  				j[new_date[i].toString()]=users[i];
  				
 			}
 			var cal = new CalHeatMap();
 			cal.init({
 			     itemSelector: "#all",
 			     domain: "day",
 			     subDomain: "x_hour",
 			     
 			     data: j,
 			     start: new Date(2015,10,02),
 			    cellSize: 70,
 		         cellPadding: 10,
 		         domainGutter: 25,
 		         range: 2,
 		        nextSelector: "#next",
 		        previousSelector: "#previous",
 			    onClick: function(date, nb) {
 					$("#sub_all").html("<br/><b>" +
 						date + "</b> <br/>with <b>" +
 						(nb === null ? "unknown" : nb) + "</b> Students"
 					);
 				}
 			});	
     		});	
 		document.getElementById("form_id").submit();
     }
	
	
	function TimeData(){
 		var tableData = '<table id="newtry"><tr><th>Campus</th><th>Building</th><th>Room Number</th><th>Day</th><th>Date</th><th>Year</th><th>Average Users</th><th>Registerd Users</th></tr>';
 		var c = document.getElementById("classroom3").value;
 		var x = document.getElementById("dates").value;
 		var d = new Date(x)
 		var y = document.getElementById("times1").value;
 		var z = document.getElementById("times2").value;
 		var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
 	                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
 	                         ];
 		var z1 = z.split(":")
 	    var y1 = y.split(":")
 	    var newt = 0
 	    
 	    var days = d.getDate();
        if(days < 10){
        	var days = '0'+days;
        }
        
 	   	var newd = (monthNames[d.getMonth()] +" "+ days +" "+ d.getFullYear());
	   	var path = "/datime/"+c+"/"+newd+"/"+y+"/"+z
	   	
	   	if (z1[0]>y1[0]){
	   		newt=1
	    }
	    else if (z1[0]==y1[0]&&z1[1]>y1[1]){
	    	newt=1
	    }
		
	    else{
	    	alert("Please Enter first time greater than second")
	    }   
	   	if (newt == 1){
	   	$.getJSON(path,function(data){
	   		if (!data[0]) {
        		alert("Sorry, Data is not in the Database!!!!");
        	}
        	else{
       	$.each(data, function(index, new_data) {
       		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td></tr>';
       		});

       		$('#time').html(tableData);
        	}
   			});
	   	document.getElementById("form_id3").submit()
	   	}
 	}
 	
 	function LectureData(){
 		var newtableData = '<table><tr><th>Classroom</th><th>Module</th><th>Date</th><th>Time</th><th>Associated credit count</th><th>Authenticated credit count</th></tr>';
 	    var lid = document.getElementById("lectr").value;
 		
 		
	   	var path = "/lectureclass/"+lid;

	   	
	   	$.getJSON(path,function(data){
       	$.each(data, function(index, new_data) {
       		 newtableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td></tr>';
       		});

       		$('#lect').html(newtableData);
   			});
	   	document.getElementById("form_id4").submit();
	   	
 	}
