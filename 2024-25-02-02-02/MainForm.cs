<<<<<<< HEAD
using System.Diagnostics;

namespace _2024_25_02_02_02
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Debug.WriteLine("the form was loaded");
        }
        private void MainForm_Formclosing(object sender, FormClosingEventArgs e)
        {
            Debug.WriteLine("the form is closing");
        }
        private void UpdateFormTitleButton_MouseClick(object sender, EventArgs e)
        {

        }

        private void LaunchEvenOdd_Click(object sender, EventArgs e)
        {
            EvenOddForm evenOddForm = new EvenOddForm();
            evenOddForm.ShowDialog(this);
        }

        private void SecretNumberButton_Click(object sender, EventArgs e)
        {
            SecretNumberForm secretNumberForm = new SecretNumberForm();
            secretNumberForm.ShowDialog(this);
        }

        private void LaunchDigitCounterButton_Click(object sender, EventArgs e)
        {
            DigitCounterForm digitCounterForm = new DigitCounterForm();
            digitCounterForm.ShowDialog(this);
        }

        private void FizzBuzzButton_Click(object sender, EventArgs e)
        {
            FizzBuzzForm fizzBuzzForm = new FizzBuzzForm();
            fizzBuzzForm.ShowDialog(this);
        }
    }


}

=======
using System.Diagnostics;

namespace _2024_25_02_02_02
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Debug.WriteLine("the form was loaded");
        }
        private void MainForm_Formclosing(object sender, FormClosingEventArgs e)
        {
            Debug.WriteLine("the form is closing");
        }
        private void UpdateFormTitleButton_MouseClick(object sender, EventArgs e)
        {

            }
        }

    }
}
>>>>>>> 5fbb11c84b48e987882ca2921804fcc11afbfb62
