// creating variable table data to contain the table data
var tableData = '<table><tr><th>Campus</th><th>Building</th><th>Room Number</th><th>Day</th><th>Date</th><th>Time</th><th>Year</th><th>Associated credit count</th><th>Authenticated credit count</th><th>Average Users</th></tr>';

	// Function to get all the json data and dispay as html table
 	function AllData(){
 		var c = document.getElementById("classroom").value;
 		var path = "/json1/"+c
 		$.getJSON(path,function(data){
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td><td>'+new_data[9]+'</td></tr>';
        		});

        		$('#all').html(tableData);
    	});
     }
 	
	// Function to get json data according to the day and classroom and display on html
 	function DayData(){
 		var c = document.getElementById("classroom1").value;
 		var x = document.getElementById("newday").value;
 		var path = "/day/"+c+"/"+x
 		$.getJSON(path,function(data){
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td><td>'+new_data[9]+'</td></tr>';
        		});

        		$('#day').html(tableData);
    	});
 		document.getElementById("form_id1").submit()
 	}
 	
	// Function to get json data as per the date and display as html table
 	function DateData(){
 		var c = document.getElementById("classroom2").value;
 		var x = document.getElementById("newdate").value;
        var d = new Date(x)
        var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                         ];
        
        var days = d.getDate();
        if(days < 10){
        	var days = '0'+days;
        }
        
        var newd = (monthNames[d.getMonth()] +" "+ days+" "+ d.getFullYear());
        var path = "/date/"+c+"/"+newd
       
        
        $.getJSON(path,function(data){
        	if (!data[0]) {
        		alert("Sorry, Data is not in the Database!!!!");
        	}
        	else{
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td><td>'+new_data[9]+'</td></tr>';
        	});
        	
        	$('#date').html(tableData);
        	}
    	});
        
		document.getElementById("form_id2").submit()   
    }
 	
	// Function to display json data as html table data according to the time and date 
 	function TimeData(){
 		var tableData1 = '<table><tr><th>Campus</th><th>Building</th><th>Room Number</th><th>Day</th><th>Date</th><th>Year</th><th>Average Users</th><th>Registerd Users</th></tr>';
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
       		 tableData1 += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td></tr>';
       		});

       		$('#time').html(tableData1);
        	}
   			});
	   	document.getElementById("form_id3").submit()
	   	}
 	}
 	
	// Function  to display json data as HTML data according to the lecture
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
	   	document.getElementById("form_id4").submit()
	   	
}

