import org.junit.Test;

public class SomeClass {

    @Test
    public void test1(){
        int value=2;
        int value2=3;
        assert value+value2==5;
    }
    @Test
    public void test2() {
        int value = 4;
        int value2 = 5;
        assert value + value2 == 9;
    }
}
