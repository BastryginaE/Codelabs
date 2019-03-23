using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace LanguageTutor
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

     

       

        private void button1_Click_1(object sender, EventArgs e)
        {
            Form3.ActiveForm.Hide();
            Form1 firstForm = new Form1();
            firstForm.Show();
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form3.ActiveForm.Hide();
            Form4 fourthForm = new Form4();
            fourthForm.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form3.ActiveForm.Hide();
            Form4 fourthForm = new Form4();
            fourthForm.Show();
        }
    }
}
