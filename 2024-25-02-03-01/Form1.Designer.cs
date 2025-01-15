namespace _2024_25_02_03_01
{
    partial class Form1
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
            splitContainer1 = new SplitContainer();
            BoxesLabel = new Label();
            groupBox1 = new GroupBox();
            flowLayoutPanel1 = new FlowLayoutPanel();
            AddBoxButton = new Button();
            ItemCheckBox = new CheckedListBox();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.Panel2.SuspendLayout();
            splitContainer1.SuspendLayout();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // splitContainer1
            // 
            splitContainer1.Dock = DockStyle.Fill;
            splitContainer1.Location = new Point(0, 0);
            splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.Controls.Add(BoxesLabel);
            splitContainer1.Panel1.Controls.Add(groupBox1);
            splitContainer1.Panel1.Controls.Add(AddBoxButton);
            // 
            // splitContainer1.Panel2
            // 
            splitContainer1.Panel2.Controls.Add(ItemCheckBox);
            splitContainer1.Size = new Size(1623, 773);
            splitContainer1.SplitterDistance = 540;
            splitContainer1.TabIndex = 0;
            // 
            // BoxesLabel
            // 
            BoxesLabel.AutoSize = true;
            BoxesLabel.Font = new Font("Segoe UI", 48F, FontStyle.Regular, GraphicsUnit.Point, 0);
            BoxesLabel.Location = new Point(33, -19);
            BoxesLabel.Name = "BoxesLabel";
            BoxesLabel.Size = new Size(321, 128);
            BoxesLabel.TabIndex = 0;
            BoxesLabel.Text = "Boxes:";
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(flowLayoutPanel1);
            groupBox1.Location = new Point(12, 108);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(380, 653);
            groupBox1.TabIndex = 1;
            groupBox1.TabStop = false;
            groupBox1.Text = "groupBox1";
            groupBox1.Enter += groupBox1_Enter;
            // 
            // flowLayoutPanel1
            // 
            flowLayoutPanel1.Location = new Point(15, 71);
            flowLayoutPanel1.Name = "flowLayoutPanel1";
            flowLayoutPanel1.Size = new Size(344, 557);
            flowLayoutPanel1.TabIndex = 0;
            // 
            // AddBoxButton
            // 
            AddBoxButton.Location = new Point(412, 3);
            AddBoxButton.Name = "AddBoxButton";
            AddBoxButton.Size = new Size(125, 103);
            AddBoxButton.TabIndex = 0;
            AddBoxButton.Text = "Add Box";
            AddBoxButton.UseVisualStyleBackColor = true;
            AddBoxButton.Click += AddBoxButton_Click;
            // 
            // ItemCheckBox
            // 
            ItemCheckBox.FormattingEnabled = true;
            ItemCheckBox.Items.AddRange(new object[] { "item1", "item2", "item3", "item4" });
            ItemCheckBox.Location = new Point(278, 169);
            ItemCheckBox.Name = "ItemCheckBox";
            ItemCheckBox.Size = new Size(443, 340);
            ItemCheckBox.TabIndex = 0;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1623, 773);
            Controls.Add(splitContainer1);
            Name = "Form1";
            Text = "Form1";
            splitContainer1.Panel1.ResumeLayout(false);
            splitContainer1.Panel1.PerformLayout();
            splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
            groupBox1.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer splitContainer1;
        private Button AddBoxButton;
        private Label BoxesLabel;
        private GroupBox groupBox1;
        private FlowLayoutPanel flowLayoutPanel1;
        private CheckedListBox ItemCheckBox;
    }
}
