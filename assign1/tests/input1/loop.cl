class Main {
    main() : Int {
       {
            a : Int;
            b : Int;
            c : Int;
            d : Int;
            for ({d <- 0; a <- 0;}; a < 10; a <- a+1) loop
            {
                for (b <- 0; b < 10; b <- b+1) loop
	            {
	                for (c <- 0; c < 10; c <- c+1) loop
		               d <- d + 1
		            pool;
	            }
	            pool;
            }
            pool;
            return 0;
        }
    };
};
