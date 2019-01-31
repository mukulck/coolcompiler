class Main {
  main() : Int {
    {
      bro : Int <- 0;
      c : String;
      case c of
        "a" : String => {bro <- 1; break;};
        "b" : String => {bro <- 1; break;};
        "c" : String => {bro <- 1; break;};
        "d" : String => {bro <- 1; break;};
        "e" : String => {bro <- 1; break;};
      esac;
      return 0;
    }
  };
};
