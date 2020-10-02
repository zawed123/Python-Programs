
# https://www.facebook.com/anisha.sheikh.714/posts/2627834770863645
# Subscribed by  Dilip Jackson    
int fib(int n) 
{ 
    if (n <= 1) 
        return n; 
    return fib(n-1) + fib(n-2); 
} 
  
int main () 
{ 
    int n = 9; 
    cout << fib(n); 
    getchar(); 
    return 0; 
} 
