package _5_sorts

func BubbleSort(li []int) {
	for i := 0; i < len(li)-1; i++ {
		flag := false
		for j := 0; j < len(li)-i-1; j++ {
			if li[j] > li[j+1] {
				li[j], li[j+1] = li[j+1], li[j]
				flag = true
			}
		}
		if !flag {
			return
		}
	}
}


func InsertSort(li []int){
	for i:=1;i<len(li);i++{
		tmp:=li[i]
		j:=i-1
		for ;j>=0;j--{
			if li[j]>tmp{
				li[j+1]=li[j]
			}else {
				break
			}
		}
		li[j+1]=tmp
	}
}

func SelectSort(li []int){
	for i:=0;i<len(li)-1;i++{
		minLoc := i
		for j:=i+1;j<len(li);j++{
			if li[j]<li[minLoc]{
				minLoc=j

			}
		}
		li[i],li[minLoc] = li[minLoc],li[i]
	}
}