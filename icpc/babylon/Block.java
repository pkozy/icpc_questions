public class Block implements Comparable<Block> {
    public int length;
    public int width;
    public int x;
    public int y;
    public int area;
    public int rightmost;
    public int topmost;
    
    public Block(int length, int width){
        this.length = length;
        this.width = width;
        this.x = -1;
        this.y = -1;
        this.area = length*width;
        this.rightmost = -1;
        this.topmost = -1;
        }
        
    public void setPos(int x, int y)  {
        this.x = x;
        this.y = y;
        this.rightmost = x + width;
        this.topmost = y + length;
    } 
    
    public void swapcoords(){
        int temp = x;
        x = y;
        y = temp;
    }
    
    public int countPlace(Block other) {
        if(this.area > other.area){
            return 0;
        }
        int count = 0;
       // int loopLengthx = other.width - other.x;
        //int loopLengthy = other.length - other.y;
        for(int xcrd = other.x; xcrd < other.rightmost; xcrd++){
            for(int ycrd = other.y; ycrd < other.topmost; ycrd++){
                System.out.println("x: " + xcrd + " y: " + ycrd);
                if(this.tryPlace(other,xcrd,ycrd)){
                    count++;
                }
                if(this.isSwappable()) {
                    System.out.println("hi");
                    this.swapcoords();
                    if(tryPlace(other,xcrd,ycrd)){
                        count++;
                    }
                    this.swapcoords();
                }
            }
        }
        return count;
    }
    
    public boolean tryPlace(Block other, int xcrd, int ycrd){
        this.setPos(xcrd,ycrd);
        if (this.rightmost > other.rightmost) {
            return false;
        }
        if (this.topmost > other.topmost){
            return false;
        }
        else{
            return true;
        }
        
    }
    
    public boolean isSwappable() {
        return this.width != this.length;
    }
    
    public String toString() {
        return "l: " + length + " w: " + width + " x: " + x + " y: " + y;
    }
    
   public int compareTo(Block other) {
        other = (Block) other;
        int i = 1;
        int j = (int) i;
        return (int) other.area - (int) this.area;
    }
}

