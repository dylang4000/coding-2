namespace _2024_25_02_03_01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void AddBoxButton_Click(object sender, EventArgs e)
        {
            Label label1 = new Label()
            {
                Text = "&First Name",
                Location = new Point(10, 10),
                TabIndex = 10
            };

            TextBox field1 = new TextBox()
            {
                Location = new Point(label1.Location.X, label1.Bounds.Bottom + Padding.Top),
                TabIndex = 11
            };

            Controls.Add(label1);
            Controls.Add(field1);
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {
            
        }
    }
}
