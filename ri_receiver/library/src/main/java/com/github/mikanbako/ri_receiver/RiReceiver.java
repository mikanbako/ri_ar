/* Copyright (c) 2016 Keita Kita
 *
 * This software is released under the MIT License.
 * http://opensource.org/licenses/mit-license.php
 */

package com.github.mikanbako.ri_receiver;

/**
 * Interface that receives infrared rays.
 */
interface RiReceiver {
    /**
     * Call when infrared rays.
     *
     * @param id ID of this infrared rays.
     */
    void onRiReceive(int id);
}
