const test1 = [ 60, 50, 95, 80, 70 ];
const test2 = [0, 100, 20, 50, 30];

const getMaxValue = (arr) => {
  for(let i=0; i<arr.length-1; i++) {
    if(arr[i]  > arr[i+1]) {
      const tmp = arr[i];
      arr[i] = arr[i+1];
      arr[i+1] = tmp;
    }
  }
  return arr[arr.length-1];
};

console.log('test1: ', getMaxValue(test1));
console.log('test2: ', getMaxValue(test2));