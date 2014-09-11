  // This defines the variables shown in the sliders. 
  // Note that there is a possible namespace conflict with JavaScript globals
  var sliders = [
                 { 'human_name'   : 'Middle:',
                   'machine_name' : 'm', 
                   'min'      : 0,
                   'max'      : 50, 
                   'value'    : 33
                 },
                 { 'human_name'   : 'Young:',
                   'machine_name' : 'y', 
                   'min'      : 0,
                   'max'      : 50, 
                   'value'    : 50
                 }
                 ] 

  var x = 0;
  var flotplot = 0; 

  function plot() {
    var_o = 100-var_y-var_m
    total = (var_y*2+var_m*5+var_o*8)/100;
    if(var_o>=0) { 
      $('#plot_info').text(""+var_y+"%\u00D72/1000 + "+var_m+"%\u00D75/1000 + "+var_o+"%\u00D78/1000 = "+total+"/1000 deaths per visit");
      $('#death_rate').text("Total death rate is "+total+" per thousand visits");
    } else {
      $('#plot_info').text("Total of young and middle-aged people greater than 100%. Move your sliders down.");
      $('#death_rate').text('');
    }
    $('#old').text(var_o+"%");
  }

  function replot(event,ui) {
    //alert("replot");
    for (var s in sliders) {
      value = $("#"+sliders[s]["machine_name"]).slider("option","value");
      mname = sliders[s]["machine_name"];
      $("#ctr_"+mname).html(value+"%");
      window["var_"+mname] = value;
    }
    plot();
  }

  $(function(){ 
    for (var s in sliders) {
      $("#applet").append($("<tr><td>"+sliders[s]["human_name"]+"</td>"+
                            "<td width=50><div id=ctr_"+sliders[s]["machine_name"]+"></div></td>"+
                            "<td width=400><div id="+sliders[s]["machine_name"]+"></div></td>"+
                            "</tr>"));
      slider = $("#"+sliders[s]["machine_name"]).slider({'max':sliders[s]["max"], 
                                                         'min':sliders[s]["min"], 
                                                         'value':sliders[s]["value"], 
                                                         slide:function(){replot();},
                                                         change:function(){replot();}});
      $("#ctr_"+sliders[s]["machine_name"]).html("0");
      
    }

    replot();
  });
