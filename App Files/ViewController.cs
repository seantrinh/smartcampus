using System;
//using System.Data.SqlClient;
using UIKit;
//using MySql;
//using MySql.Data;
//using MySql.Data.MySqlClient;
//using MySql.Data.MySqlClient.Replication;

namespace test3
{
    public partial class ViewController : UIViewController
    {
		//string connectionString = @"Server=<192.168.1.151>;Database=<demo1>;User Id=<sam>;Password=<sam>;Trusted_Connection=true";
		//string databaseTable = "<temprecord>";

		//MySql.Data.MySqlClient.MySqlConnection mySqlConnection;

		//string connectionString = @"server=127.0.0.1;" + @"uid=root;" + @"pwd=vesonder;" + @"database=test1;";

        protected ViewController(IntPtr handle) : base(handle)
        {
			// Note: this .ctor should not contain any initialization logic.
			
        }

        public override void ViewDidLoad()
        {
            base.ViewDidLoad();
			

			//mySqlConnection = new MySqlConnection();
			//mySqlConnection.ConnectionString = connectionString;
			//mySqlConnection.Open();
			//mySqlConnection.Close();

			//textbox1.Text = "hello";
			/*
            string selectQuery = String.Format("SELECT * FROM {0}", databaseTable);
			using (SqlConnection connection = new SqlConnection(connectionString))
			{
				//open connection
				connection.Open();
				SqlCommand command = new SqlCommand(selectQuery, connection);
				command.Connection = connection;
				command.CommandText = selectQuery;
				var result = command.ExecuteReader();
				textbox1.Text = command.ToString();
                connection.Close();
			}
            
            try
            {
                //string selectQuery = "SELECT * FROM Database";
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {

                    conn.Open();
                    //MySqlCommand cmd = new MySqlCommand(selectQuery, conn);

                    //string data = cmd.ToString();
                    textbox1.Text = "hello";
                    conn.Close();
                }


            }

            catch(Exception ex)
            {
                textbox1.Text = ex.ToString();
            }
*/
        }

        public override void DidReceiveMemoryWarning()
        {
            base.DidReceiveMemoryWarning();
            // Release any cached data, images, etc that aren't in use.
        }



    }

}
