#include "dwm_api.h"
#include <stdio.h>

int main() {
   dwm_loc_data_t loc;
   int rv, i;

   // Initialize the library
   dwm_init();

   rv = dwm_loc_get(&loc);
   if (rv != 0) {
       printf("Error: %d\n", rv);
       return rv;
   }

   // Check if position data is available
   if (loc.pos_available) {
       printf("Position: [%ld, %ld, %ld, %u]\n", loc.pos.x, loc.pos.y, loc.pos.z, loc.pos.qf);
   } else {
       printf("Position data not available\n");
   }

   // Iterate through anchors and get distances
   for (i = 0; i < loc.anchors.dist.cnt; ++i) {
       printf("Anchor %u: Address: 0x%04x, Distance: %lu mm, Quality: %u\n", i, loc.anchors.dist.addr[i], loc.anchors.dist.dist[i], loc.anchors.dist.qf[i]);

       if (i < loc.anchors.an_pos.cnt) {
           printf("Anchor Position: [%ld, %ld, %ld, %u]\n", loc.anchors.an_pos.pos[i].x, loc.anchors.an_pos.pos[i].y, loc.anchors.an_pos.pos[i].z, loc.anchors.an_pos.pos[i].qf);
       }
   }

   return 0;
}