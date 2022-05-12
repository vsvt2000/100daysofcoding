package main

import(
	"fmt"
)

type Stack struct{

	
	arr []int
	top int
	size int
	maxsize int
}

func newStack(s int) *Stack {
	sampl:=[]int{8}
	for i:=0;i<s;i++{
		sampl=append(sampl,0)
	}
	sampl=sampl[1:]
	return &Stack{
	  arr:sampl,
	  top:-1,
	  size:0,
	  maxsize:s,
	}
  }

func (stack *Stack) push(element int){
	temp:=*stack
	if (temp.size+1>temp.maxsize) && (temp.size>0){
		fmt.Println("Stack Full Exception-push")
	}else{

		temp.top=temp.top+1
		temp.size=temp.size+1
		temp.arr[temp.top]=element
		*stack=temp
	}
}

func (stack *Stack) pop() int{
	temp:=*stack
	if temp.top==-1{
		fmt.Println("Stack Empty Exception-pop")
		return -404
	}else{
		var element=temp.arr[temp.top]
		temp.arr[temp.top]=0
		temp.top= temp.top-1
		temp.size= temp.size-1
		*stack=temp
		return element
	}
}

func (stack Stack) getTop() int{
	
	if stack.top==-1{
		fmt.Println("Stack Empty Exception-gettop")
		return -404
	}else{
		var element=stack.arr[stack.top]
		return element
	}
}

func (stack Stack) isEmpty() bool{
	
	if stack.top==-1{
		return true
	}else{
		return false
	}
}

func (stack Stack) printStack(){
	
	if stack.isEmpty(){
		fmt.Println("Stack Empty Exception-print")
	}else{
		fmt.Printf("stack=%v\n", stack.arr)
	}
}



func main(){
	var s *Stack 
	s = newStack(5)
	x:=*s
	fmt.Println(x.isEmpty())
	s.push(10)
	x=*s
	s.push(20)
	x=*s
	s.push(30)
	x=*s
	s.push(40)
	x=*s
	s.push(50)
	x=*s
	s.push(10)
	x=*s
	fmt.Println(x.getTop())
	x.printStack()
	s.pop()
	x=*s
	fmt.Println(x.getTop())
	x.printStack()

}
