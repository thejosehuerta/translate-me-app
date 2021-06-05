// choices box for the translate portion of the website
const translate_choices = new Choices('#choices1');
 
// choices for the chart creator portion of the website
const chart_choices = new Choices('#choices2', {
    removeItemButton: true,  
});

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
  });


// function print_values() {
//     const lang_values = []
//     const values = chart_choices.getValue(true);
//     lang_values.push(values)
//     for (let index = 0; index < lang_values.length; index++) {
//         // print to html element with id 'test
//         document.getElementById('test').innerHTML = lang_values[index];
//     }
// }

