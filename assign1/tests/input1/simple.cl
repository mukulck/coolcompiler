class Main {
	main() : Int {
		{
			i : Int <- 6;
                if (i>=0) then
                    out_string("yes\n")
                else
                    out_string("no\n")
                fi;

            pool;
		}
	};
};
