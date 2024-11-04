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
