// WARNING
//
// This file has been generated automatically by Visual Studio from the outlets and
// actions declared in your storyboard file.
// Manual changes to this file will not be maintained.
//
using Foundation;
using System;
using System.CodeDom.Compiler;

namespace test3
{
    [Register ("ViewController")]
    partial class ViewController
    {
        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UIImageView IconSound1 { get; set; }

        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UIImageView IconSound2 { get; set; }

        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UILabel lblname { get; set; }

        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UILabel textbox1 { get; set; }

        void ReleaseDesignerOutlets ()
        {
            if (IconSound1 != null) {
                IconSound1.Dispose ();
                IconSound1 = null;
            }

            if (IconSound2 != null) {
                IconSound2.Dispose ();
                IconSound2 = null;
            }

            if (lblname != null) {
                lblname.Dispose ();
                lblname = null;
            }

            if (textbox1 != null) {
                textbox1.Dispose ();
                textbox1 = null;
            }
        }
    }
}