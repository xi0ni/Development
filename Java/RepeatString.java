public class RepeatString {

    public static class HasRepeat {
        String str;

        public HasRepeat(String str) {
            this.str = str;
        }

        public boolean checkRepeat() {
            for (int i = 0; i < this.str.length(); i++) {
                String placeholder = this.str.substring(i, i + 1);
                for (int x = i + 1; x < this.str.length(); x++) {
                    if (placeholder.equals(this.str.substring(x, x + 1))) {
                        return true;
                    }
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        HasRepeat hasRepeatChecker = new HasRepeat("hello");
        boolean result = hasRepeatChecker.checkRepeat();
        System.out.println(result); 
    }
}
