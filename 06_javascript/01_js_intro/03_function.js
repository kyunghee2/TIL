// //선언식 
// console.log(add(1,2))
// function add(num1,num2){
//   return num1+num2
// }
// console.log(add(1,2))

// //표현식
// //console.log(sub(2,3)) //에러-> Cannot access 'sub' before initialization
// const sub = function(num1,num2){
//   return num1 - num2
// }
// console.log(sub(2,3))

// //타입 확인하면 둘 다 function으로 동일, 작동 방법만 다름
// console.log(typeof add)
// console.log(typeof sub)

//화살표 함수 (Arrow function)
const iot1 = function(name){
  return `hello ${name}!!`
}
//1. function 키워드 삭제
const iot1 = (name) => {return `hello ${name}`}
//2. () 생략 (함수 매개변수 하나일 경우)
const iot1 = name => {return `hello ${name}`}
//3. {}, return 생략(바디에 표현식 1개)
const iot1 = name => `hello ${name}`

//[실습] 3단계에 걸쳐 화살표 함수로 바꿔보기
let square = function(num){
	return num ** 2
}
//1. function 키워드 삭제
let square = (num)=>{return num ** 2}
//2. () 생략 (함수 매개변수 하나일 경우)
let square = num => {return num ** 2}
//3. {}, return 생략(바디에 표현식 1개)
let square = num => num ** 2
//console.log(square(2))

//4. 인자가 없다면? () 혹은 _로 표시 가능
let noArgs = () => 'No args!!!'
noArgs = _ => 'No args!!!'
//5-1 object를 return을 명시적으로 적어준다
let returnObject = () => {return {key:'value'}}
console.log(returnObject())
console.log(typeof returnObject())
//5-2 return을 적지 않으려면 괄호 붙이기
returnObject = () => ({key:'value'})
console.log(returnObject())
console.log(typeof returnObject())

//6. 기본 인자 부여하기 (Default Args)
//인자 개수와 상관없이 반드시 괄호를 붙인다
const sayHello = (name='혁진') => `hi! ${name}`


