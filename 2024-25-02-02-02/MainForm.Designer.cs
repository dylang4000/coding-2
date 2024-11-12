<<<<<<< HEAD
﻿
namespace _2024_25_02_02_02
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            EvenOdd = new Button();
            SecretNumberButton = new Button();
            LaunchDigitCounterButton = new Button();
            FizzBuzzButton = new Button();
            SuspendLayout();
            // 
            // EvenOdd
            // 
            EvenOdd.Location = new Point(133, 75);
            EvenOdd.Name = "EvenOdd";
            EvenOdd.Size = new Size(226, 74);
            EvenOdd.TabIndex = 0;
            EvenOdd.Text = "EVEN/ODD";
            EvenOdd.UseVisualStyleBackColor = true;
            EvenOdd.Click += LaunchEvenOdd_Click;
            // 
            // SecretNumberButton
            // 
            SecretNumberButton.Location = new Point(133, 223);
            SecretNumberButton.Name = "SecretNumberButton";
            SecretNumberButton.Size = new Size(226, 74);
            SecretNumberButton.TabIndex = 3;
            SecretNumberButton.Text = "Launch Secret number";
            SecretNumberButton.UseVisualStyleBackColor = true;
            SecretNumberButton.Click += SecretNumberButton_Click;
            // 
            // LaunchDigitCounterButton
            // 
            LaunchDigitCounterButton.Location = new Point(133, 297);
            LaunchDigitCounterButton.Name = "LaunchDigitCounterButton";
            LaunchDigitCounterButton.Size = new Size(226, 74);
            LaunchDigitCounterButton.TabIndex = 4;
            LaunchDigitCounterButton.Text = "Launch Digit Counter";
            LaunchDigitCounterButton.UseVisualStyleBackColor = true;
            LaunchDigitCounterButton.Click += LaunchDigitCounterButton_Click;
            // 
            // FizzBuzzButton
            // 
            FizzBuzzButton.Location = new Point(133, 148);
            FizzBuzzButton.Name = "FizzBuzzButton";
            FizzBuzzButton.Size = new Size(226, 74);
            FizzBuzzButton.TabIndex = 5;
            FizzBuzzButton.Text = "FizzBuzzButton";
            FizzBuzzButton.UseVisualStyleBackColor = true;
            FizzBuzzButton.Click += FizzBuzzButton_Click;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            ClientSize = new Size(490, 431);
            Controls.Add(FizzBuzzButton);
            Controls.Add(LaunchDigitCounterButton);
            Controls.Add(SecretNumberButton);
            Controls.Add(EvenOdd);
            ForeColor = SystemColors.ActiveCaptionText;
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "First WinForms App";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button EvenOdd;
        private Button SecretNumberButton;
        private Button LaunchDigitCounterButton;
        private Button FizzBuzzButton;
    }
}
=======
﻿
namespace _2024_25_02_02_02
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            Namelabl = new Label();
            NameTextBox = new TextBox();
            ChangeFormTextButton = new Button();
            OutputListBox = new ListBox();
            SuspendLayout();
            // 
            // Namelabl
            // 
            Namelabl.AutoSize = true;
            Namelabl.Location = new Point(287, 77);
            Namelabl.Name = "Namelabl";
            Namelabl.Size = new Size(59, 25);
            Namelabl.TabIndex = 0;
            Namelabl.Text = "Name";
            // 
            // NameTextBox
            // 
            NameTextBox.Location = new Point(228, 105);
            NameTextBox.Name = "NameTextBox";
            NameTextBox.PlaceholderText = "your name here...";
            NameTextBox.Size = new Size(172, 31);
            NameTextBox.TabIndex = 1;
            // 
            // ChangeFormTextButton
            // 
            ChangeFormTextButton.Location = new Point(200, 142);
            ChangeFormTextButton.Name = "ChangeFormTextButton";
            ChangeFormTextButton.Size = new Size(232, 133);
            ChangeFormTextButton.TabIndex = 2;
            ChangeFormTextButton.Text = "Update";
            ChangeFormTextButton.UseVisualStyleBackColor = true;
            ChangeFormTextButton.Click += UpdateFormTitleButton_MouseClick;
            // 
            // OutputListBox
            // 
            OutputListBox.FormattingEnabled = true;
            OutputListBox.ItemHeight = 25;
            OutputListBox.Location = new Point(228, 281);
            OutputListBox.Name = "OutputListBox";
            OutputListBox.Size = new Size(180, 104);
            OutputListBox.TabIndex = 3;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            ClientSize = new Size(632, 462);
            Controls.Add(OutputListBox);
            Controls.Add(ChangeFormTextButton);
            Controls.Add(NameTextBox);
            Controls.Add(Namelabl);
            ForeColor = SystemColors.ActiveCaptionText;
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "First WinForms App";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }



        #endregion

        private Label Namelabl;
        private TextBox NameTextBox;
        private Button ChangeFormTextButton;
        private ListBox OutputListBox;
    }
}
>>>>>>> 5fbb11c84b48e987882ca2921804fcc11afbfb62
