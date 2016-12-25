/* Copyright (c) 2016 Keita Kita
 *
 * This software is released under the MIT License.
 * http://opensource.org/licenses/mit-license.php
 */

using UnityEngine;
using System.Collections.Generic;

public sealed class ApplicationController : MonoBehaviour
{
    // Update is called once per frame
    private void Update()
    {
        if (Input.GetKey(KeyCode.Escape))
        {
            Application.Quit();
        }
    }
}
