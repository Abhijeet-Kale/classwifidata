/**
 * 
 */
var tableData = '<table><tr><th>Campus</th><th>Building</th><th>Room Number</th><th>Day</th><th>Date</th><th>Time</th><th>Year</th><th>Associated credit count</th><th>Authenticated credit count</th></tr>';

 	function AllData(){
 		var c = document.getElementById("classroom").value;
 		var path = "/json1/"+c
 		$.getJSON(path,function(data){
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td></tr>';
        		});

        		$('#all').html(tableData);
    	});
     }
 	
 	function DayData(){
 		var c = document.getElementById("classroom1").value;
 		var x = document.getElementById("newday").value;
 		var path = "/day/"+c+"/"+x
 		$.getJSON(path,function(data){
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td></tr>';
        		});

        		$('#day').html(tableData);
    	});
 		document.getElementById("form_id1").submit()
 	}
 	
 	function DateData(){
 		var c = document.getElementById("classroom2").value;
 		var x = document.getElementById("newdate").value;
        var d = new Date(x)
        var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                         ];
        var newd = (monthNames[d.getMonth()] +" "+ d.getDate()+" "+ d.getFullYear());
        var path = "/date/"+c+"/"+newd
       
        
        $.getJSON(path,function(data){
        	$.each(data, function(index, new_data) {
        		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td></tr>';
        	});
        	$('#date').html(tableData);
    	});
        
		document.getElementById("form_id2").submit()   
    }
 	
 	function TimeData(){
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
 	    
 	   	var newd = (monthNames[d.getMonth()] +" "+ d.getDate()+" "+ d.getFullYear());
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
       	$.each(data, function(index, new_data) {
       		 tableData += '<tr><td>'+new_data[0]+'</td><td>'+new_data[1]+'</td><td>'+new_data[2]+'</td><td>'+new_data[3]+'</td><td>'+new_data[4]+'</td><td>'+new_data[5]+'</td><td>'+new_data[6]+'</td><td>'+new_data[7]+'</td><td>'+new_data[8]+'</td></tr>';
       		});

       		$('#time').html(tableData);
   			});
	   	document.getElementById("form_id3").submit()
	   	}
 	}
