const canvas =   document.getElementById('myChart'); 
var ctx = canvas.getContext('2d');


function changeArrayToInt(array){
    const myArray = []
    for (let index = 0; index < array.length; index++) {
        const element = parseInt(array[index]);
        myArray.push(element)    
    }
    return myArray
}


const newLabels = changeArrayToInt(labels); 
const newData = changeArrayToInt(data);

// function changeArraysToArrayOfObjects(array1,array2){
//     const myArray = []
//     for (let index = 0; index < array1.length; index++) {
//         const d = {}; 
//         const element1 = parseInt(array1[index]);
//         const element2 = parseInt(array2[index]);
//         d['x'] = element1
//         d['y'] = element2
//         myArray.push(d)
//     }
//     return myArray
// }

// const scatterDataset = changeArraysToArrayOfObjects(newLabels,newData); 


var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels,
        datasets:[{
            label: '#Total Population', 
            data: newData
        }]
    },
    options: {
        responsive: true,
        scales: {
          xAxes: [{
            ticks: {
              maxRotation: 90,
              minRotation: 80
            }
          }],
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        }
      }
});