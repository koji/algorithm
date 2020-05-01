const test1 = [60, 50, 95, 80, 70];
const test2 = [0, 100, 20, 50, 30];

const bubbleSort = (arr) => {
  for(let i=0; i<arr.length-1; i++) {
    for(let j=0; j<arr.length-1; j++) {
      if(arr[j] > arr[j+1]) {
        const tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }
    }
  }
  return arr;
}

console.log('test1: ', bubbleSort(test1));
console.log('test2: ', bubbleSort(test2));