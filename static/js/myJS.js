const newData = []

for (let index=0; index<data.length;index++){
    const currentData = data[index]; 
    const sData = {}
    sData["country"] =currentData["country"]
    sData["total cases"] = currentData["total cases"]
    sData["new cases"] = currentData["new cases"]
    sData["total deaths"] = currentData["total deaths"]
    sData["total recovered"] = currentData["total recovered"]
    sData["serious"] = currentData["serious"]
    newData.push(sData)
}


const dropDownSelector = document.getElementsByClassName('dropDownSelector')[0]; 
const allSelectorsDropDown = document.getElementsByClassName('dropdown-item'); 
let sortBy = null ;

for (let index = 0; index < allSelectorsDropDown.length; index++) {
    const element = allSelectorsDropDown[index];
    
    element.addEventListener('click',function(){
        sortBy = allSelectorsDropDown[index].textContent
        dropDownSelector.innerHTML = sortBy 
    }) 
}

function sortByKey(array, key,ascending=true) {
    return array.sort(function(a, b) {
        let x = a[key]; 
        let y = b[key];
        if (ascending)
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
        else {
            return ((x > y) ? -1 : ((x < y) ? 1 : 0));
        }
        
    });
}

sortedArray = sortByKey(newData,'total cases',false)

const tableBody = document.getElementsByClassName('tableBodyHolder')[0]; 
const tableRow = document.getElementsByClassName('tableRowHolder')[0]; 
const tableDataHolder = document.getElementsByClassName('tableDataHolder');


// for (let index = 0; index < sortedArray.length; index++) {
    
//     tableBody.appendChild(tableRow); 
//     const itemValues = Object.values(sortedArray[index]); 
//     for(let secondIndex = 0; secondIndex<itemValues.length; secondIndex++   )
//     {
//         tableDataHolder[secondIndex].innerHTML= itemValues[secondIndex]
//     }
// }