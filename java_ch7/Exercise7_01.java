import java.util.Scanner;

public class Exercise7_01 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of students: ");

        int classSize = input.nextInt();
        int[] classScores = new int[classSize];

        System.out.print("Enter " + classSize + " scores: ");

        for (int i=0; i < classSize; i++) {
            classScores[i] = input.nextInt();
        }

        int maxScore = bestScore(classScores);

        for (int i=0; i < classSize; i++) {
            System.out.println("Student " + i + " score is " + classScores[i] + " and grade is " + letterGrade(classScores[i], maxScore));
        }
    }

    public static String letterGrade(int score, int best) {
        if (score > (best - 10))
            return "A";
        else if (score > (best - 20))
            return "B";
        else if (score > (best -30))
            return "C";
        else if (score > (best - 40))
            return "D";
        else
            return "F";
    }

    public static Integer bestScore(int... classScores) {
        int maxScore = 0;
        for (int i=0; i < classScores.length; i++){
            if (classScores[i] > maxScore)
                maxScore = classScores[i];
        }
        return maxScore;
    }

}