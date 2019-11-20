const userName = prompt('니 이름은 뭐니?')
let message = ''

if(userName === '도현'){
  message = '유단자여...'
}else if(userName === '혁진'){
  message = '<h1>감자...</h1>'
}else{
  message = `<h1>${userName}..누구??</h1>`
}
document.write(message)