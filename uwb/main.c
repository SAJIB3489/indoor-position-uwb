
void on_dwm_evt(dwm_evt_t *p_evt)
{

        uint8_t len;
        uint8_t i;
        // Current Idc to store in data (2 bytes for id, 4bytes for timestamp)
        uint8_t idx = 6;
        // TimeStamp
        uint32_t tim;


        switch (p_evt->header.id) {
        /* New location data */
        case DWM_EVT_LOC_READY:

                tim=dwm_systime_us_get();
                //IOT
                memcpy(data_out+2,&tim,4);

                memcpy(data_out+idx,&(p_evt->loc.anchors.dist.cnt),1);
                idx = idx + 1;
               // console
                printf("\nT:%lu (0x%lx)\ti:%u",tim,tim, p_evt->loc.anchors.dist.cnt);


                for (i = 0; i < p_evt->loc.anchors.dist.cnt; ++i)
                {
                        memcpy(data_out+idx,&(p_evt->loc.anchors.dist.addr[i]),2);
                        idx = idx + 2;
                        memcpy(data_out+idx,&(p_evt->loc.anchors.dist.dist[i]),4);
                        idx = idx + 4;

                        printf("\tID:%04X\tDist:%ld", p_evt->loc.anchors.dist.addr[i], p_evt->loc.anchors.dist.dist[i]);
                                }

                dwm_evt_listener_register(
                        DWM_EVT_LOC_READY | DWM_EVT_USR_DATA_READY | DWM_EVT_USR_DATA_SENT |
                        DWM_EVT_BH_INITIALIZED_CHANGED |
                        DWM_EVT_UWBMAC_JOINED_CHANGED, NULL);

                // write just 31!
                dwm_usr_data_write(data_out,31,false);

                break;
...