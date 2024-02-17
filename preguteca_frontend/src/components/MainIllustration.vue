<script lang="ts" setup>
import image1 from "../assets/main-illustration/img/main_illustration_v31.png";
import image2 from "../assets/main-illustration/img/main_illustration_v32.png";
import image3 from "../assets/main-illustration/img/main_illustration_v33.png";
import image4 from "../assets/main-illustration/img/main_illustration_v34.png";
import image5 from "../assets/main-illustration/img/main_illustration_v35.png";
import image6 from "../assets/main-illustration/img/main_illustration_v36.png";
import image7 from "../assets/main-illustration/img/main_illustration_v37.png";
import image8 from "../assets/main-illustration/img/main_illustration_v38.png";
import image9 from "../assets/main-illustration/img/main_illustration_v39.png";
import image10 from "../assets/main-illustration/img/main_illustration_v310.png";
import image11 from "../assets/main-illustration/img/main_illustration_v311.png";
import image12 from "../assets/main-illustration/img/main_illustration_v312.png";
import image13 from "../assets/main-illustration/img/main_illustration_v313.png";
import image14 from "../assets/main-illustration/img/main_illustration_v314.png";
import image15 from "../assets/main-illustration/img/main_illustration_v315.png";
import image16 from "../assets/main-illustration/img/main_illustration_v316.png";
import image17 from "../assets/main-illustration/img/main_illustration_v317.png";
import image18 from "../assets/main-illustration/img/main_illustration_v318.png";
import image19 from "../assets/main-illustration/img/main_illustration_v319.png";
import image20 from "../assets/main-illustration/img/main_illustration_v320.png";
import image21 from "../assets/main-illustration/img/main_illustration_v321.png";
import image22 from "../assets/main-illustration/img/main_illustration_v322.png";
import image23 from "../assets/main-illustration/img/main_illustration_v323.png";
import image24 from "../assets/main-illustration/img/main_illustration_v324.png";
import image25 from "../assets/main-illustration/img/main_illustration_v325.png";
import image26 from "../assets/main-illustration/img/main_illustration_v326.png";
import image27 from "../assets/main-illustration/img/main_illustration_v327.png";
import image28 from "../assets/main-illustration/img/main_illustration_v328.png";
import image29 from "../assets/main-illustration/img/main_illustration_v329.png";
import image30 from "../assets/main-illustration/img/main_illustration_v330.png";
import image31 from "../assets/main-illustration/img/main_illustration_v331.png";
import image32 from "../assets/main-illustration/img/main_illustration_v332.png";
import image33 from "../assets/main-illustration/img/main_illustration_v333.png";
import image34 from "../assets/main-illustration/img/main_illustration_v334.png";
import image35 from "../assets/main-illustration/img/main_illustration_v335.png";
import image36 from "../assets/main-illustration/img/main_illustration_v336.png";
import image37 from "../assets/main-illustration/img/main_illustration_v337.png";
import image38 from "../assets/main-illustration/img/main_illustration_v338.png";
import image39 from "../assets/main-illustration/img/main_illustration_v339.png";
import image40 from "../assets/main-illustration/img/main_illustration_v340.png";
import image41 from "../assets/main-illustration/img/main_illustration_v341.png";
import image42 from "../assets/main-illustration/img/main_illustration_v342.png";
import image43 from "../assets/main-illustration/img/main_illustration_v343.png";
import image44 from "../assets/main-illustration/img/main_illustration_v344.png";
import image45 from "../assets/main-illustration/img/main_illustration_v345.png";
import image46 from "../assets/main-illustration/img/main_illustration_v346.png";
import image47 from "../assets/main-illustration/img/main_illustration_v347.png";
import image48 from "../assets/main-illustration/img/main_illustration_v348.png";
import image49 from "../assets/main-illustration/img/main_illustration_v349.png";
import image50 from "../assets/main-illustration/img/main_illustration_v350.png";

import { computed, onMounted, reactive, ref } from "vue";
import { updateActiveCategory, updateActivePanel } from "../store";
import { useCategories } from "../queries/useCategories";

const categoryName = ref("");
const categories = reactive(useCategories());
const category = computed(() =>
  categories.data?.find((cat) => cat.name === categoryName.value)
);

onMounted(() => {
  const clickables = document.querySelectorAll("*[data-clickable='true']");
  const tagTextList = document.querySelectorAll("#etiquetes text");

  // Adjust the translateY for the text in the tags
  tagTextList.forEach((text) => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    //@ts-ignore
    (text as HTMLElement).transform.baseVal[0].matrix.f += 4;
  });

  for (const clickable of clickables) {
    (clickable as HTMLElement).addEventListener("click", (event: MouseEvent) => {
      if (!event.target) return;
      const elem = event.currentTarget as HTMLElement;
      event.preventDefault();
      event.stopPropagation();
      if (elem.dataset) {
        console.log(elem)
        categoryName.value = elem.dataset.categoryName ?? "";
        console.log(categoryName.value)
        if (category.value) {
          console.log("ok")
          updateActiveCategory(category.value);
          updateActivePanel("category")
        }
      }
    });
  }
});
const noiseFrequency = ref(1.0)
const numOctaves = ref(3)
setInterval(() => {
  noiseFrequency.value = Math.random() * 0.1 + 0.2
}, 200);

</script>
<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1125 7625">
    <filter id='noiseFilter'>
      <feTurbulence type='fractalNoise' :baseFrequency='noiseFrequency' :numOctaves='numOctaves' stitchTiles='stitch' />
    </filter>
    <defs>
      <clipPath id="clip-path">
        <polygon class="cls-1"
          points="305.98 566.29 305.98 593.8 209.59 649.45 63.27 564.97 63.27 537.46 111.47 492.17 159.66 481.82 305.98 566.29" />
      </clipPath>
      <clipPath id="clip-path-2">
        <polygon class="cls-1"
          points="935.26 513.82 935.26 531.93 869.97 569.63 869.97 581 813.38 613.66 813.38 683.6 731.72 636.45 731.72 537.04 853.6 466.67 894.42 467.24 935.26 513.82" />
      </clipPath>
      <clipPath id="clip-path-3">
        <polygon class="cls-1"
          points="646.87 758.13 646.87 814.03 577.37 854.16 577.37 918.65 505.1 876.93 505.1 756.53 574.61 716.41 646.87 758.13" />
      </clipPath>
      <clipPath id="clip-path-4">
        <polygon class="cls-1"
          points="1057.55 897.2 1057.55 1006.43 964.38 1060.22 964.38 981.18 894.66 940.92 894.66 910.74 941.24 851.26 987.83 856.95 1057.55 897.2" />
      </clipPath>
      <clipPath id="clip-path-5">
        <polygon class="cls-1"
          points="311.84 958.51 311.84 998.79 238.13 1041.34 238.13 1133.54 149.39 1082.3 149.39 950.04 223.28 907.38 274.95 937.21 311.84 958.51" />
      </clipPath>
      <clipPath id="clip-path-6">
        <polygon class="cls-1"
          points="722.74 1071.08 722.74 1199.72 623.29 1257.14 623.29 1147.84 507.84 1081.18 507.84 1061.84 557.56 1013.78 607.28 1004.42 722.74 1071.08" />
      </clipPath>
      <clipPath id="clip-path-7">
        <polygon class="cls-1"
          points="252.91 1279.99 252.91 1309.69 171.65 1356.61 171.65 1440.08 103.42 1400.68 103.42 1287.52 184.69 1240.59 252.91 1279.99" />
      </clipPath>
      <clipPath id="clip-path-8">
        <polygon class="cls-1"
          points="542.99 1451.53 542.99 1494.78 480.4 1530.91 480.4 1618.46 387.56 1564.86 387.56 1434.06 450.14 1397.93 542.99 1451.53" />
      </clipPath>
      <clipPath id="clip-path-9">
        <polygon class="cls-1"
          points="944.73 1675.46 944.73 1722.26 865.75 1767.86 865.75 1841.28 787.95 1796.36 787.95 1676.14 866.92 1630.54 905.83 1634.39 944.73 1675.46" />
      </clipPath>
      <clipPath id="clip-path-10">
        <polygon class="cls-1"
          points="239.69 1729.89 239.69 1774.95 165.57 1817.75 165.57 1910.83 80.05 1861.45 80.05 1723.31 154.17 1680.51 196.93 1683.28 239.69 1729.89" />
      </clipPath>
      <clipPath id="clip-path-11">
        <polygon class="cls-1"
          points="627.31 1666.22 627.31 1796.02 562.28 1833.57 562.28 1734.3 475.05 1683.94 475.05 1653.4 540.08 1615.86 627.31 1666.22" />
      </clipPath>
      <clipPath id="clip-path-12">
        <polygon class="cls-1"
          points="372.8 2032 372.8 2046.44 298.68 2089.24 298.68 2181.43 209.94 2130.2 209.94 2023.56 284.06 1980.76 328.43 1980.76 372.8 2032" />
      </clipPath>
      <clipPath id="clip-path-13">
        <polygon class="cls-1"
          points="783 2099.61 783 2247.61 683.55 2305.01 683.55 2209.36 625.82 2148.91 568.1 2142.7 568.1 2090.38 667.54 2032.95 783 2099.61" />
      </clipPath>
      <clipPath id="clip-path-14">
        <polygon class="cls-1"
          points="1046.55 1956.05 1046.55 1986.37 966.75 2032.44 901.08 1994.52 901.08 1949.77 980.88 1903.7 1046.55 1956.05" />
      </clipPath>
      <clipPath id="clip-path-15">
        <polygon class="cls-1"
          points="1026.91 2161.24 1026.91 2192.43 949.91 2236.88 949.91 2363.62 846.06 2303.66 846.06 2145.73 923.05 2101.28 974.89 2131.2 1026.91 2161.24" />
      </clipPath>
      <clipPath id="clip-path-16">
        <polygon class="cls-1"
          points="438.52 2336.25 438.52 2446.18 374.46 2483.16 374.46 2399.3 302.26 2357.62 288.24 2365.71 274.22 2359.72 274.22 2324.18 305.58 2283.47 338.28 2278.38 438.52 2336.25" />
      </clipPath>
      <clipPath id="clip-path-17">
        <polygon class="cls-1"
          points="230.73 2484.12 230.73 2566.59 169.61 2601.68 87.48 2554.27 87.48 2471.99 148.61 2436.71 230.73 2484.12" />
      </clipPath>
      <clipPath id="clip-path-18">
        <polygon class="cls-1"
          points="1055.69 2491.08 1055.69 2631.15 966.83 2682.46 966.83 2570.69 843.91 2499.72 843.91 2471.43 932.78 2420.12 1055.69 2491.08" />
      </clipPath>
      <clipPath id="clip-path-19">
        <polygon class="cls-1"
          points="733.47 2420.89 733.47 2465.91 629.52 2525.92 629.52 2652.8 533.29 2597.25 533.29 2425.34 637.24 2365.33 733.47 2420.89" />
      </clipPath>
      <clipPath id="clip-path-20">
        <path class="cls-1"
          d="M684.49,2803v-95.17C680.9,2653.32,598,2607,499.3,2604.45c-93.65-2.45-168.79,35.47-172.2,86.89v95.17l-.06,1c0,.13,0,.25,0,.38q-2.65,57.24,87.5,90.88,91.28,34.05,182.55,8.42T684.49,2803Zm-126-3.31a317.81,317.81,0,0,1-70.76.61l-95.25-55,85.18-49.18,130.1,75.11Z" />
      </clipPath>
      <clipPath id="clip-path-21">
        <polygon class="cls-1"
          points="246.02 2765.67 246.02 2877.91 159.86 2927.65 159.86 2839.87 91.74 2800.54 91.74 2776.09 177.9 2726.34 246.02 2765.67" />
      </clipPath>
      <clipPath id="clip-path-22">
        <polygon class="cls-1"
          points="341.36 3140.73 341.36 3167.66 281.95 3201.96 161.8 3132.59 161.8 3105.66 191.51 3080.09 221.21 3071.36 341.36 3140.73" />
      </clipPath>
      <clipPath id="clip-path-23">
        <polygon class="cls-1" points="1125 2739.46 1125 2960.07 0 3609.59 0 3388.98 1125 2739.46" />
      </clipPath>
      <clipPath id="clip-path-24">
        <polygon class="cls-1"
          points="791.8 3271.05 791.8 3311.11 717.9 3353.77 717.9 3445.97 629.16 3394.73 629.16 3262.48 703.05 3219.81 703.06 3219.81 791.8 3271.05" />
      </clipPath>
      <clipPath id="clip-path-25">
        <polygon class="cls-1"
          points="449.99 3484.29 449.99 3518.77 377.83 3560.44 377.83 3639.57 291.47 3589.71 291.47 3476.09 363.63 3434.43 449.99 3484.29" />
      </clipPath>
      <clipPath id="clip-path-26">
        <polygon class="cls-1"
          points="262.05 3742.41 262.05 3884.9 171.58 3937.13 171.58 3821.43 39.37 3745.1 39.37 3718.31 84.51 3665.36 129.74 3665.36 262.05 3742.41" />
      </clipPath>
      <clipPath id="clip-path-27">
        <polygon class="cls-1"
          points="904.43 3747.21 904.43 3787.28 830.53 3829.94 830.53 3922.13 741.79 3870.9 741.79 3738.64 815.69 3695.98 867.35 3725.81 904.43 3747.21" />
      </clipPath>
      <clipPath id="clip-path-28">
        <polygon class="cls-1"
          points="987.82 4034.83 987.82 4177.31 899.35 4228.39 899.35 4112.69 815.4 4064.22 815.4 4037.43 903.87 3986.36 987.82 4034.83" />
      </clipPath>
      <clipPath id="clip-path-29">
        <path class="cls-1"
          d="M649.79,3976.91q-2.64,40-75.46,35.16t-70.16-44.8q-.27-44.61,39.27-65.27t76,5Q655.94,3932.71,649.79,3976.91Z" />
      </clipPath>
      <clipPath id="clip-path-30">
        <polygon class="cls-1"
          points="235.25 4138.66 235.25 4161.12 158.76 4205.27 158.76 4316.01 64.81 4261.76 64.81 4128.56 141.28 4084.41 235.25 4138.66" />
      </clipPath>
      <clipPath id="clip-path-31">
        <polygon class="cls-1"
          points="728.54 4188.05 728.54 4305.2 675.62 4335.75 675.62 4357.61 661.77 4365.61 661.77 4247.52 585.14 4203.28 585.14 4182.36 620.64 4161.87 651.92 4143.81 728.54 4188.05" />
      </clipPath>
      <clipPath id="clip-path-32">
        <polygon class="cls-1"
          points="1024.48 4431.63 1024.48 4458.81 932.53 4511.9 932.53 4598.62 847 4549.23 847 4435.34 938.96 4382.25 981.72 4385.02 1024.48 4431.63" />
      </clipPath>
      <clipPath id="clip-path-33">
        <polygon class="cls-1"
          points="212.21 4486.67 212.21 4625.1 131.88 4671.48 131.88 4554.05 64.83 4515.34 64.83 4494.34 145.17 4447.96 212.21 4486.67" />
      </clipPath>
      <clipPath id="clip-path-34">
        <polygon class="cls-1"
          points="539.78 4840.44 539.78 4970.81 485.83 5001.96 485.83 5008.32 475.67 5014.2 475.67 4923.2 394.96 4876.6 394.96 4830.87 459.08 4793.85 539.78 4840.44" />
      </clipPath>
      <clipPath id="clip-path-35">
        <polygon class="cls-1"
          points="254.75 4752.31 254.75 4794.53 178.29 4838.68 178.29 4923.51 85.45 4869.91 85.45 4742.86 161.91 4698.71 254.75 4752.31" />
      </clipPath>
      <clipPath id="clip-path-36">
        <polygon class="cls-1"
          points="1059.19 5089.86 1059.19 5218.5 959.74 5275.92 959.74 5193.82 837.92 5123.49 837.92 5076.94 887.64 5028.89 937.37 5019.53 1059.19 5089.86" />
      </clipPath>
      <clipPath id="clip-path-37">
        <polygon class="cls-1"
          points="746.52 5024.68 746.52 5047.99 660.46 5097.67 660.46 5201.9 574.58 5152.31 574.58 5024.78 660.64 4975.1 703.58 4972.32 746.52 5024.68" />
      </clipPath>
      <clipPath id="clip-path-38">
        <path class="cls-1"
          d="M363.56,5293.61v-85.14c-2.25-34.11-54.12-63.07-115.87-64.68s-110,24.72-107.75,58.84v80.66q-2.41,36.44,54.7,57.75t114.22,5.27Q366,5330.28,363.56,5293.61Zm-58.7-31.37c-35,8.78-77.43,6.2-111.39-6.78-11.14-11.73-10.48-25.34,1.73-35.65,18.73-15.81,58.47-19.14,88.75-7.42S323.6,5246.42,304.86,5262.24Z" />
      </clipPath>
      <clipPath id="clip-path-39">
        <polygon class="cls-1"
          points="937.33 5506.63 937.33 5533.95 844.79 5587.37 763.63 5540.51 763.63 5502.6 793.18 5469.07 820.73 5469.63 862.75 5493.89 889 5478.74 937.33 5506.63" />
      </clipPath>
      <clipPath id="clip-path-40">
        <polygon class="cls-1"
          points="420.16 5832.17 420.16 5859.48 219.21 5975.5 143.82 5931.97 143.82 5904.66 344.77 5788.65 382.46 5796.65 420.16 5832.17" />
      </clipPath>
      <clipPath id="clip-path-41">
        <polygon class="cls-1"
          points="974.79 5760.07 974.79 5779.53 870.78 5844.4 789.62 5797.53 789.62 5773.26 841.62 5727.85 894.35 5713.64 974.79 5760.07" />
      </clipPath>
      <clipPath id="clip-path-42">
        <path class="cls-1"
          d="M622.09,6161.79q-42.63,13.85-85.23-3.94t-31.93-45a287.12,287.12,0,0,0,26.8-132.5,15.12,15.12,0,0,1,.4-4.59c3.61-15,28.85-24.5,56.38-21.24s46.9,18.06,43.29,33a230.85,230.85,0,0,0,22.25,132.19Q664.7,6147.93,622.09,6161.79Z" />
      </clipPath>
      <clipPath id="clip-path-43">
        <polygon class="cls-1"
          points="1028.04 6244.84 1028.04 6265.5 922.83 6326.25 847.65 6282.84 847.65 6247.11 952.87 6201.44 1028.04 6244.84" />
      </clipPath>
      <clipPath id="clip-path-44">
        <polygon class="cls-1"
          points="303.85 6618.83 303.85 6633.38 240.64 6669.87 164.17 6625.72 164.17 6611.17 186.72 6583.59 227.38 6574.68 303.85 6618.83" />
      </clipPath>
      <clipPath id="clip-path-45">
        <polygon class="cls-1"
          points="792.54 6756.19 792.54 6794.73 735.97 6827.39 604.8 6751.66 604.8 6729.15 661.37 6680.46 792.54 6756.19" />
      </clipPath>
      <clipPath id="clip-path-46">
        <polygon class="cls-1"
          points="1125.01 6635.5 1125.01 7625 0.01 7625 0.01 7379.28 1015.59 6792.94 0.01 6206.59 0.01 5985.98 1125.01 6635.5" />
      </clipPath>
      <clipPath id="clip-path__el_prostibulo">
        <polygon class="cls-1"
          points="1031.27 1335.24 1031.27 1362.88 1020.64 1369.02 1020.64 1403.05 980.91 1401.98 941.18 1448.92 941.18 1539.35 926.13 1530.66 926.13 1461.84 874.97 1432.31 874.97 1349.02 965.05 1297.01 1031.27 1335.24" />
      </clipPath>
      <clipPath id="clip-path__el_tribunal">
        <polygon class="cls-1"
          points="1102.71 3474.49 1102.71 3570.15 1017.18 3619.53 901.72 3552.87 901.72 3457.21 987.26 3407.83 1044.98 3414.05 1102.71 3474.49" />
      </clipPath>
      <clipPath id="clip-path__la_television">
        <polygon class="cls-1"
          points="533.21 4323.03 533.21 4440.12 453.75 4485.98 368.21 4436.6 368.21 4319.52 407.93 4272.58 447.66 4273.65 533.21 4323.03" />
      </clipPath>
      <clipPath id="clip-path__la_estacion">
        <polygon class="cls-1"
          points="931.12 4696.62 931.12 4733.71 854.53 4777.93 690.75 4683.37 690.75 4646.27 767.34 4602.06 931.12 4696.62" />
      </clipPath>
    </defs>
    <g id="fondo_negro" data-name="fondo negro">
      <rect class="cls-2" width="1125" height="7625" />
        <rect filter="url(#noiseFilter)" width="100%" height="100%" style="opacity:0.6"></rect>
    </g>
    <g id="isla1">
      <g id="LINE" class="cls-3">
        <polygon points="738.46 388.38 198.68 700.02 0 585.31 0 143.65 314.58 143.65 738.46 388.38" />
      </g>
      <g class="cls-4" data-clickable="true" data-category-name="los_jardines">
        <image width="171" height="176" loading="lazy" transform="translate(25.28 394.77) scale(1.94)" :href="image1" />
      </g>
      <g id="LINE-2" data-name="LINE">
        <polygon class="cls-1"
          points="305.98 566.29 305.98 593.8 209.59 649.45 63.27 564.97 63.27 537.46 111.47 492.17 159.66 481.82 305.98 566.29" />
      </g>
      <g>
        <g id="ARC">
          <path class="cls-5" d="M418.45,529.08A698.61,698.61,0,0,0,283.24,451" />
        </g>
        <g id="ARC-2" data-name="ARC">
          <path class="cls-5" d="M446,513.17a698.39,698.39,0,0,0-135.21-78.06" />
        </g>
        <g id="ARC-3" data-name="ARC">
          <path class="cls-5" d="M473.58,497.26a698.14,698.14,0,0,0-135.21-78.07" />
        </g>
        <g id="ARC-4" data-name="ARC">
          <path class="cls-5" d="M501.43,481.18a698.14,698.14,0,0,0-135.21-78.07" />
        </g>
        <g id="ARC-5" data-name="ARC">
          <path class="cls-5" d="M481.62,365.3a283.18,283.18,0,0,0-69.93,40.38" />
        </g>
        <g id="ARC-6" data-name="ARC">
          <path class="cls-5" d="M509.18,381.22a282.77,282.77,0,0,0-69.92,40.37" />
        </g>
        <g id="ARC-7" data-name="ARC">
          <path class="cls-5" d="M536.75,397.13a283.14,283.14,0,0,0-69.93,40.37" />
        </g>
        <g id="ARC-8" data-name="ARC">
          <path class="cls-5" d="M564.31,413.05a282.83,282.83,0,0,0-69.93,40.37" />
        </g>
        <g id="ARC-9" data-name="ARC">
          <path class="cls-5" d="M591.88,429A283.14,283.14,0,0,0,522,469.33" />
        </g>
        <g id="ARC-10" data-name="ARC">
          <path class="cls-5" d="M581.56,400.67A584.14,584.14,0,0,0,464.9,333.32" />
        </g>
        <g id="ARC-11" data-name="ARC">
          <path class="cls-5" d="M607.37,385.77A583.94,583.94,0,0,0,490.7,318.42" />
        </g>
        <g id="ARC-12" data-name="ARC">
          <path class="cls-5" d="M633.18,370.87a583.94,583.94,0,0,0-116.67-67.35" />
        </g>
        <g id="ARC-13" data-name="ARC">
          <path class="cls-5" d="M495,291.1a469.82,469.82,0,0,0-115,66.4" />
        </g>
        <g id="ARC-14" data-name="ARC">
          <path class="cls-5" d="M463.81,273.09a470.32,470.32,0,0,0-115,66.4" />
        </g>
        <g id="ARC-15" data-name="ARC">
          <path class="cls-5" d="M432.63,255.09a469.82,469.82,0,0,0-115,66.4" />
        </g>
        <g id="ARC-16" data-name="ARC">
          <path class="cls-5" d="M356.33,381.44a238.6,238.6,0,0,0-83,47.9" />
        </g>
        <g id="ARC-17" data-name="ARC">
          <path class="cls-5" d="M323.27,362.35a238.38,238.38,0,0,0-83,47.91" />
        </g>
        <g id="ARC-18" data-name="ARC">
          <path class="cls-5" d="M291.4,344a238.38,238.38,0,0,0-83,47.91" />
        </g>
        <g id="ARC-19" data-name="ARC">
          <path class="cls-5" d="M259.32,325.43a238.56,238.56,0,0,0-83,47.91" />
        </g>
        <g id="ARC-20" data-name="ARC">
          <path class="cls-5" d="M238.52,513.8A776.58,776.58,0,0,0,85.6,425.51" />
        </g>
        <g id="ARC-21" data-name="ARC">
          <path class="cls-5" d="M264.79,498.86a776.41,776.41,0,0,0-152.93-88.3" />
        </g>
        <g id="ARC-22" data-name="ARC">
          <path class="cls-5" d="M291.58,483.39A776.37,776.37,0,0,0,138.65,395.1" />
        </g>
        <g id="LINE-3" data-name="LINE">
          <line class="cls-5" x1="308.38" y1="556.55" x2="360" y2="526.75" />
        </g>
        <g id="LINE-4" data-name="LINE">
          <line class="cls-5" x1="360" y1="526.75" x2="386.88" y2="542.27" />
        </g>
        <g id="LINE-5" data-name="LINE">
          <line class="cls-5" x1="386.88" y1="542.27" x2="335.26" y2="572.07" />
        </g>
        <g id="LINE-6" data-name="LINE">
          <line class="cls-5" x1="335.26" y1="572.07" x2="308.38" y2="556.55" />
        </g>
        <g id="LINE-7" data-name="LINE">
          <line class="cls-5" x1="292.56" y1="547.42" x2="344.17" y2="517.62" />
        </g>
        <g id="LINE-8" data-name="LINE">
          <line class="cls-5" x1="344.17" y1="517.62" x2="316.69" y2="501.75" />
        </g>
        <g id="LINE-9" data-name="LINE">
          <line class="cls-5" x1="316.69" y1="501.75" x2="265.07" y2="531.55" />
        </g>
        <g id="LINE-10" data-name="LINE">
          <line class="cls-5" x1="265.07" y1="531.55" x2="292.56" y2="547.42" />
        </g>
        <g id="ARC-23" data-name="ARC">
          <path class="cls-5" d="M273,306.23a230.82,230.82,0,0,0-70.09-40.47" />
        </g>
        <g id="ARC-24" data-name="ARC">
          <path class="cls-5" d="M121.55,472.88A518.28,518.28,0,0,0,12.66,535.75" />
        </g>
        <g id="ARC-25" data-name="ARC">
          <path class="cls-5" d="M94,457A518.34,518.34,0,0,0,0,509" />
        </g>
        <g id="ARC-26" data-name="ARC">
          <path class="cls-5" d="M66.42,441.05A517.37,517.37,0,0,0,0,475.14" />
        </g>
        <g id="ARC-27" data-name="ARC">
          <path class="cls-5" d="M38.86,425.14Q19.06,433.56,0,443.6" />
        </g>
        <g id="ARC-28" data-name="ARC">
          <path class="cls-5" d="M11.3,409.22q-5.69,2.41-11.3,5" />
        </g>
        <g id="ARC-29" data-name="ARC">
          <path class="cls-5" d="M43.48,353.34Q21.27,362.79,0,374.27" />
        </g>
        <g id="ARC-30" data-name="ARC">
          <path class="cls-5" d="M15.92,337.43q-8,3.4-15.92,7.08" />
        </g>
        <g id="ARC-31" data-name="ARC">
          <path class="cls-5" d="M122.47,373.17a624.33,624.33,0,0,0-120-69.28" />
        </g>
        <g id="ARC-32" data-name="ARC">
          <path class="cls-5" d="M152,356.11A623.85,623.85,0,0,0,32,286.82" />
        </g>
        <g id="ARC-33" data-name="ARC">
          <path class="cls-5" d="M181.22,339.26A623.85,623.85,0,0,0,61.22,270" />
        </g>
        <g id="ARC-34" data-name="ARC">
          <path class="cls-5" d="M211.24,321.92a624.33,624.33,0,0,0-120-69.28" />
        </g>
        <g id="ARC-35" data-name="ARC">
          <path class="cls-5" d="M304.19,288.21a231,231,0,0,0-70.1-40.47" />
        </g>
        <g id="ARC-36" data-name="ARC">
          <path class="cls-5" d="M335.39,270.2a230.38,230.38,0,0,0-70.09-40.47" />
        </g>
        <g id="ARC-37" data-name="ARC">
          <path class="cls-5" d="M366.6,252.18a230.82,230.82,0,0,0-70.09-40.47" />
        </g>
        <g id="ARC-38" data-name="ARC">
          <path class="cls-5" d="M397.81,234.16a231,231,0,0,0-70.1-40.47" />
        </g>
        <g id="ARC-39" data-name="ARC">
          <path class="cls-5" d="M129.11,197.45a344.6,344.6,0,0,0-76.53-44.18" />
        </g>
        <g id="ARC-40" data-name="ARC">
          <path class="cls-5" d="M101.54,213.37A343.53,343.53,0,0,0,25,169.19" />
        </g>
        <g id="ARC-41" data-name="ARC">
          <path class="cls-5" d="M74,229.28A344.1,344.1,0,0,0,0,186.17" />
        </g>
        <g id="ARC-42" data-name="ARC">
          <path class="cls-5" d="M46.41,245.2A343.12,343.12,0,0,0,0,215.31" />
        </g>
        <g id="ARC-43" data-name="ARC">
          <path class="cls-5" d="M216.7,143.64a470.7,470.7,0,0,0-61.25,40.75" />
        </g>
        <g id="ARC-44" data-name="ARC">
          <path class="cls-5" d="M155.86,143.64q-16.26,10.71-31.59,22.74" />
        </g>
        <g id="ARC-45" data-name="ARC">
          <path class="cls-5" d="M99.22,143.64q-3.09,2.34-6.14,4.74" />
        </g>
        <g id="LINE-11" data-name="LINE">
          <line class="cls-5" x1="65.52" y1="413.92" x2="25.36" y2="390.73" />
        </g>
        <g id="LINE-12" data-name="LINE">
          <line class="cls-5" x1="25.36" y1="390.73" x2="65.52" y2="367.54" />
        </g>
        <g id="LINE-13" data-name="LINE">
          <line class="cls-5" x1="65.52" y1="367.54" x2="105.68" y2="390.73" />
        </g>
        <g id="LINE-14" data-name="LINE">
          <line class="cls-5" x1="105.68" y1="390.73" x2="65.52" y2="413.92" />
        </g>
      </g>
      <g>
        <g id="LINE-15" data-name="LINE">
          <line class="cls-6" x1="305.98" y1="593.8" x2="305.98" y2="566.29" />
        </g>
        <g>
          <g id="LINE-16" data-name="LINE">
            <line class="cls-7" x1="63.27" y1="564.97" x2="209.59" y2="649.45" />
          </g>
          <g id="LINE-17" data-name="LINE">
            <line class="cls-7" x1="209.59" y1="649.45" x2="305.98" y2="593.8" />
          </g>
          <g>
            <g id="LINE-18" data-name="LINE">
              <line class="cls-7" x1="111.47" y1="492.17" x2="159.66" y2="481.82" />
            </g>
            <g id="LINE-19" data-name="LINE">
              <line class="cls-7" x1="159.66" y1="481.82" x2="305.98" y2="566.29" />
            </g>
            <g>
              <g id="LINE-20" data-name="LINE">
                <line class="cls-7" x1="209.59" y1="621.94" x2="63.27" y2="537.47" />
              </g>
              <g id="LINE-21" data-name="LINE">
                <line class="cls-7" x1="209.59" y1="649.45" x2="209.59" y2="621.94" />
              </g>
              <g id="LINE-22" data-name="LINE">
                <line class="cls-7" x1="209.59" y1="621.94" x2="257.78" y2="576.65" />
              </g>
              <g id="LINE-23" data-name="LINE">
                <line class="cls-7" x1="305.98" y1="566.29" x2="257.78" y2="576.65" />
              </g>
              <g id="LINE-24" data-name="LINE">
                <line class="cls-7" x1="257.78" y1="576.65" x2="111.47" y2="492.17" />
              </g>
            </g>
            <g id="LINE-25" data-name="LINE">
              <line class="cls-7" x1="111.47" y1="492.17" x2="63.27" y2="537.47" />
            </g>
          </g>
          <g id="LINE-26" data-name="LINE">
            <line class="cls-7" x1="63.27" y1="537.47" x2="63.27" y2="564.97" />
          </g>
        </g>
      </g>
      <g>
        <g id="ELLIPSE">
          <path class="cls-6"
            d="M199.62,225.5c.57-8.6-11.66-16.41-27.32-17.45s-28.82,5.1-29.39,13.7,11.67,16.4,27.33,17.44,28.81-5.09,29.38-13.69Z" />
        </g>
        <g id="ELLIPSE-2" data-name="ELLIPSE">
          <path class="cls-6"
            d="M252.21,195.14c.57-8.6-11.67-16.41-27.33-17.45s-28.82,5.1-29.38,13.7,11.66,16.41,27.32,17.44,28.82-5.09,29.39-13.69Z" />
        </g>
        <g id="SPLINE">
          <path class="cls-6" d="M195.61,190.46l-.08,14.15" />
        </g>
        <g id="SPLINE-2" data-name="SPLINE">
          <path class="cls-6" d="M195.53,204.61q-1,15.15,26.56,17.39t30.06-12.8" />
        </g>
        <g id="SPLINE-3" data-name="SPLINE">
          <path class="cls-6" d="M252.15,209.2l.07-14.45" />
        </g>
        <g id="SPLINE-4" data-name="SPLINE">
          <path class="cls-6" d="M143,220.82,143,235" />
        </g>
        <g id="SPLINE-5" data-name="SPLINE">
          <path class="cls-6" d="M143,235q-1,15.15,26.56,17.39t30.05-12.8" />
        </g>
        <g id="SPLINE-6" data-name="SPLINE">
          <path class="cls-6" d="M199.56,239.56l.08-14.45" />
        </g>
      </g>
    </g>
    <g id="isla2">
      <g id="LINE-27" data-name="LINE">
        <polyline class="cls-8"
          points="1125 144.38 1125 266.56 1100.81 280.53 1100.81 319.21 1034.72 357.37 919.26 290.71 919.26 276.56 870.12 220.58 820.97 219.81 820.97 241.98 735.09 192.4 735.09 161.43 704.29 143.65 0 143.65" />
      </g>
    </g>
    <g id="isla3">
      <g class="cls-9" data-clickable="true" data-category-name="el_mercado">
        <image loading="lazy" width="137" height="152" transform="translate(698.14 427.83) scale(1.94)" :href="image2" />
      </g>
      <g id="LINE-28" data-name="LINE">
        <polygon class="cls-1"
          points="935.18 512.72 935.18 530.83 869.88 568.53 869.88 579.9 813.3 612.56 813.3 682.5 731.63 635.35 731.63 535.94 853.51 465.57 894.34 466.14 935.18 512.72" />
      </g>
      <g id="LINE-29" data-name="LINE">
        <line class="cls-10" x1="731.64" y1="578.09" x2="731.64" y2="636.23" />
      </g>
      <g id="LINE-30" data-name="LINE">
        <line class="cls-11" x1="756.22" y1="348.27" x2="756.22" y2="348.27" />
      </g>
      <g id="LINE-31" data-name="LINE">
        <polygon class="cls-8"
          points="1125 440.31 1125 489.8 1087.53 511.44 1087.53 493.19 1019.35 532.55 1019.35 573.97 948.56 614.84 948.56 625.55 891.98 658.22 813.31 612.79 869.88 580.13 869.89 569.41 935.18 531.72 935.18 513.61 894.35 467.02 894.19 466.83 853.35 466.27 731.64 536.32 731.64 578.09 698.2 539.8 664.77 539.48 664.77 487.21 600.28 449.99 657.2 417.12 685.04 433.19 703.85 422.32 703.85 396.52 756.22 366.3 756.22 347.76 788.33 310.2 820.44 311.19 849.61 328.04 876.16 312.7 943.8 351.75 961.41 341.6 1018.36 374.48 1018.36 409.71 1066.56 437.55 1093.39 422.06 1125 440.31" />
      </g>
      <g id="LINE-32" data-name="LINE">
        <line class="cls-10" x1="813.3" y1="683.38" x2="813.3" y2="614.33" />
      </g>
      <g id="LINE-33" data-name="LINE">
        <line class="cls-10" x1="813.3" y1="614.33" x2="813.3" y2="583.97" />
      </g>
      <g id="LINE-34" data-name="LINE">
        <line class="cls-10" x1="772.47" y1="537.38" x2="731.64" y2="536.82" />
      </g>
      <g id="LINE-35" data-name="LINE">
        <line class="cls-10" x1="935.18" y1="513.61" x2="813.3" y2="583.97" />
      </g>
      <g id="LINE-36" data-name="LINE">
        <line class="cls-10" x1="813.3" y1="583.97" x2="772.47" y2="537.38" />
      </g>
      <g id="LINE-37" data-name="LINE">
        <line class="cls-10" x1="772.47" y1="537.38" x2="894.35" y2="467.02" />
      </g>
      <line class="cls-10" x1="731.64" y1="636.23" x2="813.3" y2="683.38" />
    </g>
    <g id="isla4">
      <g id="LINE-38" data-name="LINE">
        <polygon class="cls-8"
          points="1125 563.39 1125 765.53 1096.52 749.1 1096.52 770.7 1034.88 735.11 1034.88 697.82 972.3 661.68 1041.05 621.99 1073.27 640.6 1109.54 619.64 1109.54 572.33 1125 563.39" />
      </g>
    </g>
    <g id="isla5">
      <g id="TEXT">
        <text class="cls-12" transform="matrix(1, -0.01, 0.01, 1, 60.61, 720.07)">
          5
        </text>
      </g>
      <g id="LINE-39" data-name="LINE">
        <polygon class="cls-8"
          points="344.46 785.51 313.44 785.51 282.43 821.33 282.43 796.97 220.4 832.78 220.4 865.37 154.45 903.44 154.45 844.15 109.22 844.15 63.98 896.38 63.98 923.16 0 960.1 0 658.04 31.93 626 87.43 617.6 159.02 658.93 175.78 649.26 264.12 700.26 264.12 739.13 344.46 785.51" />
      </g>
    </g>
    <g id="isla6">
      <g class="cls-13">
        <image loading="lazy" data-clickable="true" data-category-name="la_farmacia" width="100" height="113"
          transform="translate(465.66 692.92) scale(2.23)" :href="image3" />
      </g>
      <g class="cls-14">
        <image loading="lazy" data-clickable="true" data-category-name="el_banco" width="106" height="119"
          transform="translate(864.48 824.38) scale(2.23)" :href="image4" />
      </g>
      <g id="LINE-40" data-name="LINE">
        <polygon class="cls-1"
          points="1057.55 897.2 1057.55 1006.43 964.38 1060.22 964.38 981.18 894.66 940.92 894.66 910.74 941.24 851.26 987.83 856.95 1057.55 897.2" />
      </g>
      <g id="LINE-41" data-name="LINE">
        <polygon class="cls-1"
          points="646.87 758.02 646.87 813.92 577.37 854.05 577.37 918.54 505.1 876.82 505.1 756.42 574.61 716.3 646.87 758.02" />
      </g>
      <g id="LINE-42" data-name="LINE">
        <line class="cls-7" x1="505.1" y1="756.54" x2="574.6" y2="716.41" />
      </g>
      <g id="LINE-43" data-name="LINE">
        <line class="cls-7" x1="574.6" y1="716.41" x2="621.17" y2="743.3" />
      </g>
      <g id="LINE-44" data-name="LINE">
        <line class="cls-7" x1="505.1" y1="876.93" x2="505.1" y2="756.54" />
      </g>
      <g id="LINE-45" data-name="LINE">
        <line class="cls-7" x1="505.1" y1="756.54" x2="577.37" y2="798.26" />
      </g>
      <g id="LINE-46" data-name="LINE">
        <line class="cls-7" x1="577.37" y1="798.26" x2="577.37" y2="854.16" />
      </g>
      <g id="LINE-47" data-name="LINE">
        <line class="cls-7" x1="577.37" y1="918.66" x2="577.37" y2="854.16" />
      </g>
      <g id="LINE-48" data-name="LINE">
        <line class="cls-7" x1="646.87" y1="758.13" x2="577.37" y2="798.26" />
      </g>
      <g id="LINE-49" data-name="LINE">
        <polygon class="cls-8"
          points="1125 876.47 1125 887.36 1057.55 926.31 1057.55 897.2 987.83 856.94 941.24 851.26 894.66 910.74 894.66 940.92 964.38 981.17 893.47 1022.11 841.42 992.06 841.42 1006.3 790.14 976.69 790.14 911.9 721.35 872.17 721.35 907.07 683.8 871.55 646.26 863.72 646.26 893.94 577.37 854.16 646.87 814.03 646.87 758.13 621.17 743.3 636.85 734.25 636.85 697.13 664.65 668.29 692.46 665.02 717.99 679.76 745.96 663.62 781.17 683.95 819.91 661.58 854.3 681.44 883.21 664.76 933.66 693.89 933.66 755.79 969.42 776.43 990.87 764.04 1065.99 807.42 1065.99 842.41 1125 876.47" />
      </g>
      <g id="TEXT-2" data-name="TEXT">
        <text class="cls-12" transform="matrix(1, -0.01, 0.01, 1, 691.92, 760.68)">
          6
        </text>
      </g>
      <g>
        <g>
          <g id="LINE-50" data-name="LINE">
            <line class="cls-7" x1="1010.96" y1="891.52" x2="964.38" y2="950.99" />
          </g>
          <g>
            <g id="LINE-51" data-name="LINE">
              <line class="cls-15" x1="964.38" y1="950.99" x2="964.38" y2="1060.22" />
            </g>
            <g id="LINE-52" data-name="LINE">
              <line class="cls-15" x1="1057.55" y1="926.31" x2="1057.55" y2="1006.43" />
            </g>
            <g id="LINE-53" data-name="LINE">
              <line class="cls-15" x1="894.66" y1="910.74" x2="964.38" y2="950.99" />
            </g>
            <g id="LINE-54" data-name="LINE">
              <line class="cls-15" x1="941.24" y1="851.26" x2="1010.96" y2="891.52" />
            </g>
            <g id="LINE-55" data-name="LINE">
              <line class="cls-15" x1="1010.96" y1="891.52" x2="1057.55" y2="897.2" />
            </g>
          </g>
        </g>
        <line class="cls-7" x1="964.38" y1="1060.22" x2="1057.55" y2="1006.43" />
      </g>
      <line class="cls-7" x1="577.37" y1="918.66" x2="505.1" y2="876.93" />
    </g>
    <g id="isla7">
      <g class="cls-16">
        <image loading="lazy" data-clickable="true" data-category-name="la_residencia_de_ancianos" width="146"
          height="150" transform="translate(57.93 846.66) scale(2.23)" :href="image5" />
      </g>
      <g class="cls-17"  data-clickable="true" data-category-name="el_ayuntamiento">
        <image loading="lazy" width="152" height="145"
          transform="translate(461.2 971.43) scale(2.23)" :href="image6" />
      </g>
      <g id="LINE-56" data-name="LINE">
        <polygon class="cls-1"
          points="311.84 958.51 311.84 998.79 238.13 1041.34 238.13 1133.54 149.39 1082.3 149.39 950.04 223.28 907.38 274.95 937.21 311.84 958.51" />
      </g>
      <g id="LINE-57" data-name="LINE">
        <polygon class="cls-1"
          points="722.74 1071.08 722.74 1199.72 623.29 1257.14 623.29 1147.84 507.84 1081.18 507.84 1061.84 557.56 1013.78 607.28 1004.42 722.74 1071.08" />
      </g>
      <g id="LINE-58" data-name="LINE">
        <line class="cls-18" x1="149.39" y1="1082.3" x2="537.76" y2="1306.53" />
      </g>
      <g id="LINE-59" data-name="LINE">
        <line class="cls-18" x1="537.76" y1="1306.53" x2="813.15" y2="1147.53" />
      </g>
      <g id="LINE-60" data-name="LINE">
        <line class="cls-18" x1="813.15" y1="1147.53" x2="424.78" y2="923.31" />
      </g>
      <g id="LINE-61" data-name="LINE">
        <line class="cls-18" x1="424.78" y1="923.31" x2="149.39" y2="1082.3" />
      </g>
      <g id="LINE-62" data-name="LINE">
        <polygon class="cls-8"
          points="722.74 1118.03 722.74 1071.09 607.29 1004.43 557.56 1013.79 507.84 1061.84 507.84 1081.19 623.29 1147.84 537.76 1197.23 422.31 1130.57 422.31 1102.96 373.16 1046.98 324.02 1046.21 324.02 1090.93 238.14 1041.35 311.85 998.79 311.85 958.73 274.95 937.21 285.83 930.93 285.83 894.89 356.58 854.04 356.58 840.16 390.68 799.15 424.78 800.78 536.95 865.55 536.95 882.79 608.96 924.36 640.99 905.87 724.07 953.84 724.07 1014.41 813.15 1065.84 722.74 1118.03" />
      </g>
      <g>
        <g>
          <g id="LINE-63" data-name="LINE">
            <line class="cls-7" x1="623.29" y1="1147.84" x2="623.29" y2="1128.5" />
          </g>
          <g id="LINE-64" data-name="LINE">
            <line class="cls-7" x1="722.74" y1="1118.03" x2="722.74" y2="1199.73" />
          </g>
          <g id="LINE-65" data-name="LINE">
            <line class="cls-7" x1="623.29" y1="1257.14" x2="623.29" y2="1147.84" />
          </g>
          <g id="LINE-66" data-name="LINE">
            <line class="cls-7" x1="722.74" y1="1071.08" x2="673.02" y2="1080.45" />
          </g>
          <g id="LINE-67" data-name="LINE">
            <line class="cls-7" x1="673.02" y1="1080.45" x2="557.56" y2="1013.79" />
          </g>
          <g id="LINE-68" data-name="LINE">
            <line class="cls-7" x1="507.84" y1="1061.84" x2="623.29" y2="1128.5" />
          </g>
          <g id="LINE-69" data-name="LINE">
            <line class="cls-7" x1="623.29" y1="1128.5" x2="673.02" y2="1080.45" />
          </g>
        </g>
        <line class="cls-7" x1="722.74" y1="1199.73" x2="623.29" y2="1257.14" />
      </g>
      <g>
        <g id="LINE-70" data-name="LINE">
          <line class="cls-19" x1="149.39" y1="1082.3" x2="149.39" y2="950.04" />
        </g>
        <g id="LINE-71" data-name="LINE">
          <line class="cls-19" x1="149.39" y1="950.04" x2="238.14" y2="1001.28" />
        </g>
        <g id="LINE-72" data-name="LINE">
          <line class="cls-19" x1="238.14" y1="1001.28" x2="238.14" y2="1041.34" />
        </g>
        <g id="LINE-73" data-name="LINE">
          <line class="cls-19" x1="238.14" y1="1001.28" x2="311.85" y2="958.72" />
        </g>
        <g id="LINE-74" data-name="LINE">
          <line class="cls-19" x1="274.95" y1="937.21" x2="223.29" y2="907.38" />
        </g>
        <g id="LINE-75" data-name="LINE">
          <line class="cls-19" x1="223.29" y1="907.38" x2="149.39" y2="950.04" />
        </g>
        <g id="LINE-76" data-name="LINE">
          <line class="cls-19" x1="238.14" y1="1133.54" x2="238.14" y2="1041.34" />
        </g>
        <line class="cls-19" x1="149.39" y1="1082.3" x2="238.14" y2="1133.54" />
      </g>
    </g>
    <g id="isla8">
      <g class="cls-20">
        <image loading="lazy" data-clickable="true" data-category-name="como_se_habla" width="138" height="150"
          transform="translate(33.06 1195.97) scale(1.94)" :href="image7" />
      </g>
      <g id="LINE-77" data-name="LINE">
        <polygon class="cls-1"
          points="252.91 1279.99 252.91 1309.69 171.65 1356.61 171.65 1440.08 103.42 1400.68 103.42 1287.52 184.69 1240.59 252.91 1279.99" />
      </g>
      <g id="LINE-78" data-name="LINE">
        <polygon class="cls-8"
          points="457.44 1188.96 376.37 1235.77 376.37 1295.73 320.21 1328.15 320.21 1348.67 238.94 1395.59 171.64 1356.74 252.92 1309.82 252.92 1280.12 184.68 1240.72 103.41 1287.64 103.41 1305.18 42.91 1270.25 42.91 1242.36 0 1217.58 0 1061.43 20.37 1049.67 42.66 1062.54 98.63 1030.22 174.58 1074.08 174.58 1100.89 202.95 1117.27 231.32 1100.89 316.14 1149.86 316.14 1184.59 319.58 1186.57 386.44 1147.97 457.44 1188.96" />
      </g>
      <g>
        <g id="LINE-79" data-name="LINE">
          <line class="cls-7" x1="103.41" y1="1303.57" x2="103.41" y2="1400.8" />
        </g>
        <g id="LINE-80" data-name="LINE">
          <line class="cls-7" x1="171.64" y1="1327.03" x2="171.64" y2="1361.38" />
        </g>
        <g id="LINE-81" data-name="LINE">
          <line class="cls-7" x1="171.64" y1="1361.38" x2="171.64" y2="1440.2" />
        </g>
        <g id="LINE-82" data-name="LINE">
          <line class="cls-7" x1="103.41" y1="1287.64" x2="171.64" y2="1327.03" />
        </g>
        <g id="LINE-83" data-name="LINE">
          <line class="cls-7" x1="171.64" y1="1327.03" x2="252.91" y2="1280.11" />
        </g>
      </g>
      <line class="cls-7" x1="103.41" y1="1400.8" x2="171.64" y2="1440.2" />
    </g>
    <g id="isla9">
      <g class="el_prostibulo__image">
        <image loading="lazy" data-clickable="true" data-category-name="el_prostibulo" width="109" height="110"
          transform="translate(1150.59 1386.38) rotate(135) scale(3)" :href="image47" />
      </g>
      <g id="LINE-84" data-name="LINE">
        <polygon class="cls-8"
          points="1125 1224.69 1125 1384.21 1085.9 1406.79 1085.9 1440.82 1046.18 1439.75 1006.45 1486.69 941.19 1449.01 980.91 1402.07 1020.64 1403.14 1020.64 1369.11 1031.27 1362.97 1031.27 1335.33 965.05 1297.1 874.97 1349.11 874.97 1414.86 789.45 1365.48 789.45 1341.1 712.04 1296.41 712.04 1281.43 618.08 1227.19 694.56 1183.03 711.07 1192.57 774.34 1156.04 774.34 1132.63 830.59 1100.16 873.9 1125.17 893.47 1113.87 925.76 1116.45 958.06 1151.16 958.06 1170.75 977.79 1182.13 1038.04 1147.35 1106.16 1186.68 1106.16 1213.81 1125 1224.69" />
      </g>
      <g class="">
        <clipPath id="clip-path__prostibulo">
          <polygon class="cls-1"
            points="971.19 1449.01 941.19 1539.44 874.97 1414.86 874.97 1432.4 1031.27 1335.33 941.19 1387.34 " />
        </clipPath>
        <image loading="lazy" data-clickable="true" data-category-name="el_prostibulo"
          style="clip-path: url('#clip-path__prostibulo')" width="149" height="166"
          transform="translate(850.42 1200.24) scale(1.94)" :href="image9" />
      </g>
      <g>
        <g id="LINE-85" data-name="LINE">
          <line class="cls-7" x1="941.19" y1="1449.01" x2="941.19" y2="1539.44" />
        </g>
        <g id="LINE-86" data-name="LINE">
          <line class="cls-7" x1="874.97" y1="1414.86" x2="874.97" y2="1432.4" />
        </g>
        <g id="LINE-87" data-name="LINE">
          <line class="cls-7" x1="1031.27" y1="1335.33" x2="941.19" y2="1387.34" />
        </g>
        <g id="LINE-88" data-name="LINE">
          <line class="cls-7" x1="941.19" y1="1387.34" x2="941.19" y2="1449.01" />
        </g>
        <g id="LINE-89" data-name="LINE">
          <line class="cls-7" x1="874.97" y1="1349.11" x2="941.19" y2="1387.34" />
        </g>
        <g id="LWPOLYLINE">
          <line class="cls-7" x1="926.13" y1="1530.75" x2="926.13" y2="1461.93" />
        </g>
        <g id="LWPOLYLINE-2" data-name="LWPOLYLINE">
          <line class="cls-7" x1="874.97" y1="1432.4" x2="926.13" y2="1461.93" />
        </g>
        <g id="LWPOLYLINE-3" data-name="LWPOLYLINE">
          <line class="cls-7" x1="926.13" y1="1530.75" x2="941.19" y2="1539.44" />
        </g>
      </g>
    </g>
    <g id="isla10">
      <g class="cls-21">
        <image loading="lazy" data-clickable="true" data-category-name="el_cine" width="122" height="130"
          transform="translate(327.52 1368.02) scale(2.23)" :href="image8" />
      </g>
      <g id="LINE-90" data-name="LINE">
        <polygon class="cls-1"
          points="542.99 1451.53 542.99 1494.78 480.4 1530.91 480.4 1618.46 387.56 1564.86 387.56 1434.06 450.14 1397.93 542.99 1451.53" />
      </g>
      <g id="LINE-91" data-name="LINE">
        <line class="cls-7" x1="387.56" y1="1434.07" x2="480.4" y2="1487.67" />
      </g>
      <g id="LINE-92" data-name="LINE">
        <line class="cls-7" x1="480.4" y1="1618.46" x2="480.4" y2="1487.67" />
      </g>
      <g id="LINE-93" data-name="LINE">
        <line class="cls-7" x1="480.4" y1="1487.67" x2="542.98" y2="1451.54" />
      </g>
      <g id="LINE-94" data-name="LINE">
        <polygon class="cls-8"
          points="926.13 1461.93 852 1504.72 852 1572.99 785.01 1611.67 785.01 1568.23 707.63 1612.91 636.68 1571.95 636.68 1605.22 601.21 1566.31 565.74 1564.26 565.74 1580.18 480.4 1530.91 542.99 1494.78 542.99 1451.53 450.14 1397.93 387.56 1434.06 387.56 1465.55 319.25 1426.11 372.19 1395.55 395.18 1408.83 430.49 1388.45 430.49 1348.59 485.11 1317.05 510.88 1331.92 537.76 1316.39 582.64 1342.31 605.09 1329.36 644.25 1330.64 683.4 1374.58 683.4 1409.68 702.65 1420.79 751.72 1392.47 813.67 1428.24 840.73 1412.62 926.13 1461.93" />
      </g>
      <g id="LINE-95" data-name="LINE">
        <line class="cls-7" x1="387.56" y1="1465.55" x2="387.56" y2="1564.86" />
      </g>
      <g id="LWPOLYLINE-4" data-name="LWPOLYLINE">
        <line class="cls-7" x1="387.56" y1="1564.86" x2="480.4" y2="1618.46" />
      </g>
    </g>
    <g id="isla11">
      <g class="cls-22">
        <image loading="lazy" data-clickable="true" data-category-name="el_centro_computacional" width="149" height="166"
          transform="translate(723.42 1573.24) scale(1.94)" :href="image9" />
      </g>
      <g id="LINE-96" data-name="LINE">
        <polygon class="cls-1"
          points="944.73 1675.46 944.73 1722.26 865.75 1767.86 865.75 1841.28 787.95 1796.36 787.95 1676.14 866.92 1630.54 905.83 1634.39 944.73 1675.46" />
      </g>
      <g id="LINE-97" data-name="LINE">
        <polygon class="cls-8"
          points="1125 1457.23 1125 1908.14 1094.19 1890.37 1094.19 1821.36 1007.97 1771.58 1007.97 1819.63 969.06 1775.66 930.15 1774.7 930.15 1804.7 865.74 1767.52 944.72 1721.92 944.72 1675.12 905.82 1634.05 866.92 1630.19 866.92 1611.45 940.79 1568.81 977.88 1590.21 1006.45 1573.71 1006.45 1525.67 1125 1457.23" />
      </g>
      <g id="TEXT-3" data-name="TEXT">
        <text class="cls-12" transform="matrix(1, -0.01, 0.01, 1, 1019.83, 1732.66)">
          <tspan class="cls-23">1</tspan>
          <tspan x="30.62" y="0">1</tspan>
        </text>
      </g>
      <g>
        <g id="LINE-98" data-name="LINE">
          <line class="cls-7" x1="787.95" y1="1796.02" x2="787.95" y2="1675.8" />
        </g>
        <g id="LINE-99" data-name="LINE">
          <line class="cls-7" x1="826.85" y1="1679.65" x2="865.74" y2="1720.71" />
        </g>
        <g id="LINE-100" data-name="LINE">
          <line class="cls-7" x1="865.74" y1="1720.71" x2="944.72" y2="1675.11" />
        </g>
        <g id="LINE-101" data-name="LINE">
          <line class="cls-7" x1="865.74" y1="1767.52" x2="865.74" y2="1840.94" />
        </g>
        <g id="LINE-102" data-name="LINE">
          <line class="cls-7" x1="866.93" y1="1630.2" x2="787.95" y2="1675.8" />
        </g>
        <g id="LINE-103" data-name="LINE">
          <line class="cls-7" x1="787.95" y1="1675.8" x2="826.85" y2="1679.65" />
        </g>
        <g id="LINE-104" data-name="LINE">
          <line class="cls-7" x1="826.85" y1="1679.65" x2="905.82" y2="1634.05" />
        </g>
        <g id="LINE-105" data-name="LINE">
          <line class="cls-7" x1="865.74" y1="1720.71" x2="865.74" y2="1767.52" />
        </g>
        <g id="LWPOLYLINE-5" data-name="LWPOLYLINE">
          <line class="cls-7" x1="865.74" y1="1840.94" x2="787.95" y2="1796.02" />
        </g>
      </g>
    </g>
    <g id="isla12">
      <g class="cls-24">
        <image loading="lazy" data-clickable="true" data-category-name="la_universidad" width="101" height="117"
          transform="translate(44.56 1644.29) scale(2.23)" :href="image10" />
      </g>
      <g class="cls-25">
        <image loading="lazy" data-clickable="true" data-category-name="la_escuela" width="119" height="133"
          transform="translate(437.55 1588.79) scale(1.94)" :href="image11" />
      </g>
      <g id="LINE-106" data-name="LINE">
        <polygon class="cls-1"
          points="239.69 1729.89 239.69 1774.95 165.57 1817.75 165.57 1910.83 80.05 1861.45 80.05 1723.31 154.17 1680.51 196.93 1683.28 239.69 1729.89" />
      </g>
      <g id="LINE-107" data-name="LINE">
        <polygon class="cls-1"
          points="627.31 1666.22 627.31 1796.02 562.28 1833.57 562.28 1734.3 475.05 1683.94 475.05 1653.4 540.08 1615.86 627.31 1666.22" />
      </g>
      <g id="LINE-108" data-name="LINE">
        <line class="cls-7" x1="627.31" y1="1796.02" x2="627.31" y2="1666.22" />
      </g>
      <g id="LINE-109" data-name="LINE">
        <line class="cls-7" x1="627.31" y1="1666.22" x2="540.08" y2="1615.86" />
      </g>
      <g id="LINE-110" data-name="LINE">
        <line class="cls-7" x1="80.04" y1="1723.27" x2="122.8" y2="1726.03" />
      </g>
      <g id="LINE-111" data-name="LINE">
        <line class="cls-7" x1="122.8" y1="1726.03" x2="165.56" y2="1772.64" />
      </g>
      <g id="LINE-112" data-name="LINE">
        <line class="cls-7" x1="80.04" y1="1861.41" x2="80.04" y2="1775.65" />
      </g>
      <g id="LINE-113" data-name="LINE">
        <polygon class="cls-8"
          points="492.49 1774.59 492.49 1742.97 439.19 1773.75 439.19 1826.73 376.5 1862.92 376.5 1823.75 336.77 1827.92 297.04 1869.62 231.78 1831.94 231.78 1855.94 165.56 1817.71 239.68 1774.92 239.68 1729.85 196.92 1683.24 154.16 1680.48 80.04 1723.27 80.04 1775.65 2.64 1730.97 2.64 1691.01 0 1689.49 0 1603.11 51 1573.66 51 1505.13 109.14 1471.57 136.97 1487.63 178.4 1463.71 206.98 1480.21 238.94 1461.76 303.53 1499.05 303.53 1548.64 323.26 1560.03 383.51 1525.24 466.53 1573.18 466.53 1600.31 516.77 1629.32 475.05 1653.41 475.05 1683.94 562.28 1734.3 492.49 1774.59" />
      </g>
      <g id="LINE-114" data-name="LINE">
        <line class="cls-7" x1="562.28" y1="1734.3" x2="562.28" y2="1703.77" />
      </g>
      <g id="LINE-115" data-name="LINE">
        <line class="cls-7" x1="122.81" y1="1726.04" x2="196.93" y2="1683.25" />
      </g>
      <g id="LINE-116" data-name="LINE">
        <line class="cls-7" x1="165.56" y1="1910.79" x2="165.56" y2="1772.64" />
      </g>
      <g id="LINE-117" data-name="LINE">
        <line class="cls-7" x1="165.56" y1="1772.64" x2="239.69" y2="1729.85" />
      </g>
      <g id="LINE-118" data-name="LINE">
        <line class="cls-7" x1="562.28" y1="1833.57" x2="562.28" y2="1734.3" />
      </g>
      <g id="LINE-119" data-name="LINE">
        <line class="cls-7" x1="475.05" y1="1653.4" x2="562.28" y2="1703.77" />
      </g>
      <g id="LINE-120" data-name="LINE">
        <line class="cls-7" x1="562.28" y1="1703.77" x2="627.31" y2="1666.22" />
      </g>
      <line class="cls-7" x1="516.77" y1="1629.32" x2="540.08" y2="1615.86" />
      <line class="cls-7" x1="80.04" y1="1861.41" x2="165.56" y2="1910.79" />
      <line class="cls-7" x1="562.28" y1="1833.57" x2="627.31" y2="1796.02" />
    </g>
    <g id="isla13">
      <g id="LINE-121" data-name="LINE">
        <polygon class="cls-8"
          points="216.72 1896.16 142.6 1938.96 142.6 1982.57 75.61 2021.25 75.61 1977.81 0 2021.46 0 1826.47 42.3 1802.04 125.62 1850.14 131.32 1846.85 174.02 1846.85 216.72 1896.16" />
      </g>
    </g>
    <g id="isla14">
      <g class="cls-26">
        <image loading="lazy" data-clickable="true" data-category-name="la_inmobiliaria" width="108" height="118"
          transform="translate(171.56 1933.94) scale(2.23)" :href="image12" />
      </g>
      <g class="cls-27">
        <image loading="lazy" data-clickable="true" data-category-name="el_hotel" width="140" height="147"
          transform="translate(516.91 2005.24) scale(2.23)" :href="image13" />
      </g>
      <g id="LINE-122" data-name="LINE">
        <polygon class="cls-1"
          points="783 2099.61 783 2247.61 683.55 2305.01 683.55 2209.36 625.82 2148.91 568.1 2142.7 568.1 2090.38 667.54 2032.95 783 2099.61" />
      </g>
      <g id="LINE-123" data-name="LINE">
        <polygon class="cls-1"
          points="372.8 2032 372.8 2046.44 298.68 2089.24 298.68 2181.43 209.94 2130.2 209.94 2023.56 284.06 1980.76 328.43 1980.76 372.8 2032" />
      </g>
      <g id="LINE-124" data-name="LINE">
        <line class="cls-7" x1="783" y1="2099.34" x2="683.55" y2="2156.76" />
      </g>
      <g id="LINE-125" data-name="LINE">
        <line class="cls-7" x1="683.84" y1="2157.04" x2="683.84" y2="2195.73" />
      </g>
      <g id="LINE-126" data-name="LINE">
        <line class="cls-7" x1="683.84" y1="2195.73" x2="683.84" y2="2305.03" />
      </g>
      <g id="LINE-127" data-name="LINE">
        <line class="cls-7" x1="783.28" y1="2165.92" x2="783.28" y2="2247.62" />
      </g>
      <g id="LINE-128" data-name="LINE">
        <polygon class="cls-8"
          points="783 2165.63 783 2099.34 667.55 2032.68 568.1 2090.1 568.1 2142.43 625.83 2148.65 683.55 2209.08 598.02 2258.46 540.29 2198.03 482.57 2191.81 482.57 2149.25 384.28 2092.51 384.28 2138.53 298.4 2088.94 372.52 2046.15 372.52 2031.71 333.01 1986.08 353.79 1974.09 353.79 1938.04 416.84 1901.64 416.84 1877.59 480.72 1840.71 597.21 1907.97 597.21 1930.39 669.22 1971.96 701.25 1953.47 742.79 1956.02 784.33 2001.44 784.33 2062 873.41 2113.43 783 2165.63" />
      </g>
      <g id="LINE-129" data-name="LINE">
        <line class="cls-7" x1="298.68" y1="2074.79" x2="298.68" y2="2089.23" />
      </g>
      <g id="LINE-130" data-name="LINE">
        <line class="cls-7" x1="568.1" y1="2090.1" x2="683.55" y2="2156.76" />
      </g>
      <g id="LINE-131" data-name="LINE">
        <line class="cls-7" x1="254.31" y1="2023.55" x2="328.43" y2="1980.76" />
      </g>
      <g id="LINE-132" data-name="LINE">
        <line class="cls-7" x1="209.94" y1="2023.55" x2="254.31" y2="2023.55" />
      </g>
      <g id="LINE-133" data-name="LINE">
        <line class="cls-7" x1="254.31" y1="2023.55" x2="298.68" y2="2074.79" />
      </g>
      <g id="LINE-134" data-name="LINE">
        <line class="cls-7" x1="298.68" y1="2074.79" x2="372.8" y2="2031.99" />
      </g>
      <g id="LINE-135" data-name="LINE">
        <line class="cls-7" x1="209.94" y1="2130.19" x2="209.94" y2="2023.55" />
      </g>
      <g id="LINE-136" data-name="LINE">
        <line class="cls-7" x1="209.94" y1="2023.55" x2="284.06" y2="1980.76" />
      </g>
      <g id="LINE-137" data-name="LINE">
        <line class="cls-7" x1="284.06" y1="1980.76" x2="328.43" y2="1980.76" />
      </g>
      <g id="LINE-138" data-name="LINE">
        <line class="cls-7" x1="298.68" y1="2089.23" x2="298.68" y2="2181.43" />
      </g>
      <g id="TEXT-4" data-name="TEXT">
        <text class="cls-12" transform="matrix(1, -0.01, 0.01, 1, 450.71, 1960.28)">
          14
        </text>
      </g>
      <g id="LWPOLYLINE-6" data-name="LWPOLYLINE">
        <line class="cls-7" x1="783.28" y1="2247.62" x2="683.84" y2="2305.03" />
      </g>
      <g id="LWPOLYLINE-7" data-name="LWPOLYLINE">
        <line class="cls-7" x1="298.68" y1="2181.43" x2="209.94" y2="2130.19" />
      </g>
      <line class="cls-7" x1="333.29" y1="1986.37" x2="328.43" y2="1980.76" />
    </g>
    <g id="isla15">
      <g class="cls-28">
        <image loading="lazy" data-clickable="true" data-category-name="el_parking" width="108" height="83"
          transform="translate(846.66 1873.78) scale(2.23)" :href="image14" />
      </g>
      <g id="LINE-139" data-name="LINE">
        <polygon class="cls-1"
          points="1046.55 1956.05 1046.55 1986.37 966.75 2032.44 901.08 1994.52 901.08 1949.77 980.88 1903.7 1046.55 1956.05" />
      </g>
      <g id="LINE-140" data-name="LINE">
        <line class="cls-7" x1="966.75" y1="2032.43" x2="966.75" y2="2002.12" />
      </g>
      <g id="LINE-141" data-name="LINE">
        <line class="cls-7" x1="1046.55" y1="1956.05" x2="966.75" y2="2002.12" />
      </g>
      <g id="LINE-142" data-name="LINE">
        <line class="cls-7" x1="966.75" y1="2002.12" x2="901.08" y2="1949.77" />
      </g>
      <g id="LINE-143" data-name="LINE">
        <line class="cls-7" x1="901.08" y1="1949.77" x2="980.88" y2="1903.7" />
      </g>
      <g id="LINE-144" data-name="LINE">
        <line class="cls-7" x1="980.88" y1="1903.7" x2="1046.55" y2="1956.05" />
      </g>
      <g id="LINE-145" data-name="LINE">
        <line class="cls-7" x1="1046.55" y1="1956.05" x2="1046.55" y2="1986.36" />
      </g>
      <g id="LINE-146" data-name="LINE">
        <line class="cls-7" x1="1046.55" y1="1986.36" x2="966.75" y2="2032.43" />
      </g>
      <g id="LINE-147" data-name="LINE">
        <line class="cls-7" x1="966.75" y1="2032.43" x2="901.08" y2="1994.52" />
      </g>
      <g id="LINE-148" data-name="LINE">
        <line class="cls-7" x1="901.08" y1="1994.52" x2="901.08" y2="1949.77" />
      </g>
    </g>
    <g id="isla16">
      <g class="cls-29">
        <image loading="lazy" data-clickable="true" data-category-name="la_bolsa" width="119" height="137"
          transform="translate(806.55 2080.99) scale(2.23)" :href="image15" />
      </g>
      <g id="LINE-149" data-name="LINE">
        <polygon class="cls-1"
          points="1026.91 2161.24 1026.91 2192.43 949.91 2236.88 949.91 2363.62 846.06 2303.66 846.06 2145.73 923.05 2101.28 974.89 2131.2 1026.91 2161.24" />
      </g>
      <g id="LINE-150" data-name="LINE">
        <line class="cls-18" x1="846.06" y1="2303.67" x2="1087.05" y2="2164.53" />
      </g>
      <g id="LINE-151" data-name="LINE">
        <line class="cls-18" x1="1087.05" y1="2164.53" x2="1125" y2="2186.44" />
      </g>
      <g id="LINE-152" data-name="LINE">
        <polygon class="cls-8"
          points="1125 2039.99 1125 2337.97 1041.6 2289.82 995.76 2239.07 949.91 2236.88 1026.9 2192.43 1026.9 2161.24 974.88 2131.21 988.62 2123.28 988.62 2074.91 1087.05 2018.08 1125 2039.99" />
      </g>
      <g id="LINE-153" data-name="LINE">
        <line class="cls-7" x1="949.91" y1="2205.69" x2="1026.9" y2="2161.24" />
      </g>
      <g id="LINE-154" data-name="LINE">
        <line class="cls-7" x1="974.88" y1="2131.21" x2="923.05" y2="2101.28" />
      </g>
      <g id="LINE-155" data-name="LINE">
        <line class="cls-7" x1="923.05" y1="2101.28" x2="846.06" y2="2145.74" />
      </g>
      <g id="LINE-156" data-name="LINE">
        <line class="cls-7" x1="846.06" y1="2303.67" x2="846.06" y2="2145.74" />
      </g>
      <g id="LINE-157" data-name="LINE">
        <line class="cls-7" x1="846.06" y1="2145.74" x2="949.91" y2="2205.69" />
      </g>
      <g id="LINE-158" data-name="LINE">
        <line class="cls-7" x1="949.91" y1="2205.69" x2="949.91" y2="2236.88" />
      </g>
      <g id="LINE-159" data-name="LINE">
        <line class="cls-7" x1="949.91" y1="2236.88" x2="949.91" y2="2363.63" />
      </g>
      <g id="LWPOLYLINE-8" data-name="LWPOLYLINE">
        <line class="cls-7" x1="949.91" y1="2363.63" x2="846.06" y2="2303.67" />
      </g>
    </g>
    <g id="isla17">
      <g class="cls-30">
        <image loading="lazy" data-clickable="true" data-category-name="el_hospital" width="118" height="121"
          transform="translate(227.26 2257.01) scale(2.23)" :href="image16" />
      </g>
      <g class="cls-31">
        <image loading="lazy" data-clickable="true" data-category-name="el_veterinario" width="109" height="110"
          transform="translate(33.42 2399.6) scale(2.23)" :href="image17" />
      </g>
      <g id="LINE-160" data-name="LINE">
        <polygon class="cls-1"
          points="438.52 2336.25 438.52 2446.18 374.46 2483.16 374.46 2399.3 302.26 2357.62 288.24 2365.71 274.22 2359.72 274.22 2324.18 305.58 2283.47 338.28 2278.38 438.52 2336.25" />
      </g>
      <g id="LINE-161" data-name="LINE">
        <polygon class="cls-1"
          points="230.73 2484.12 230.73 2566.59 169.61 2601.68 87.48 2554.27 87.48 2471.99 148.61 2436.71 230.73 2484.12" />
      </g>
      <g id="LINE-162" data-name="LINE">
        <line class="cls-7" x1="374.46" y1="2382.28" x2="374.46" y2="2483.39" />
      </g>
      <g id="LINE-163" data-name="LINE">
        <polygon class="cls-8"
          points="274.22 2324.41 274.22 2359.95 288.25 2365.95 302.27 2357.84 374.47 2399.53 295.63 2445.05 295.63 2412.57 230.73 2450.05 230.73 2483.91 148.61 2436.49 87.49 2471.78 87.49 2426.8 44.38 2377.89 0.17 2376.99 0.17 2154.89 31.03 2137.07 31.03 2089.03 129.5 2032.17 215.09 2081.59 215.09 2108.39 267.25 2115.51 319.41 2168.64 319.41 2215.43 399.98 2261.95 434.05 2242.28 517.87 2290.68 438.53 2336.49 338.29 2278.61 305.58 2283.7 274.22 2324.41" />
      </g>
      <g id="LINE-164" data-name="LINE">
        <line class="cls-7" x1="438.53" y1="2336.48" x2="438.53" y2="2446.41" />
      </g>
      <g id="LINE-165" data-name="LINE">
        <line class="cls-7" x1="87.48" y1="2554.25" x2="87.48" y2="2471.78" />
      </g>
      <g id="LINE-166" data-name="LINE">
        <line class="cls-7" x1="230.73" y1="2483.91" x2="230.73" y2="2566.38" />
      </g>
      <g id="LINE-167" data-name="LINE">
        <line class="cls-7" x1="438.53" y1="2336.48" x2="405.82" y2="2341.58" />
      </g>
      <g id="LINE-168" data-name="LINE">
        <line class="cls-7" x1="405.82" y1="2341.58" x2="374.46" y2="2382.28" />
      </g>
      <g id="LINE-169" data-name="LINE">
        <line class="cls-7" x1="374.46" y1="2382.28" x2="274.22" y2="2324.41" />
      </g>
      <g id="LINE-170" data-name="LINE">
        <line class="cls-7" x1="230.73" y1="2483.91" x2="169.61" y2="2519.2" />
      </g>
      <g id="LINE-171" data-name="LINE">
        <line class="cls-7" x1="169.61" y1="2519.2" x2="169.61" y2="2601.47" />
      </g>
      <g id="LINE-172" data-name="LINE">
        <line class="cls-7" x1="405.82" y1="2341.58" x2="305.58" y2="2283.7" />
      </g>
      <g id="LINE-173" data-name="LINE">
        <line class="cls-7" x1="169.61" y1="2519.2" x2="87.48" y2="2471.78" />
      </g>
      <g id="LWPOLYLINE-9" data-name="LWPOLYLINE">
        <line class="cls-7" x1="87.48" y1="2554.25" x2="169.61" y2="2601.47" />
      </g>
      <g id="LWPOLYLINE-10" data-name="LWPOLYLINE">
        <line class="cls-7" x1="169.61" y1="2601.47" x2="230.73" y2="2566.18" />
      </g>
      <g id="LWPOLYLINE-11" data-name="LWPOLYLINE">
        <line class="cls-7" x1="374.46" y1="2483.39" x2="438.53" y2="2446.41" />
      </g>
    </g>
    <g id="isla18">
      <g class="cls-32">
        <image loading="lazy" data-clickable="true" data-category-name="el_instituto" width="137" height="151"
          transform="translate(790.95 2379.55) scale(2.23)" :href="image18" />
      </g>
      <g class="cls-33">
        <image loading="lazy" data-clickable="true" data-category-name="el_museo" width="137" height="148"
          transform="translate(470.12 2334.99) scale(2.23)" :href="image19" />
      </g>
      <g id="LWPOLYLINE-12" data-name="LWPOLYLINE">
        <polygon class="cls-1"
          points="1055.69 2491.08 1055.69 2631.15 966.83 2682.46 966.83 2570.69 843.91 2499.72 843.91 2471.43 932.78 2420.12 1055.69 2491.08" />
      </g>
      <g id="LWPOLYLINE-13" data-name="LWPOLYLINE">
        <polygon class="cls-1"
          points="733.47 2420.89 733.47 2465.91 629.52 2525.92 629.52 2652.8 533.29 2597.25 533.29 2425.34 637.24 2365.33 733.47 2420.89" />
      </g>
      <g id="LINE-174" data-name="LINE">
        <line class="cls-7" x1="533.29" y1="2425.29" x2="629.52" y2="2480.85" />
      </g>
      <g id="LINE-175" data-name="LINE">
        <line class="cls-7" x1="629.52" y1="2480.85" x2="629.52" y2="2525.87" />
      </g>
      <g id="LINE-176" data-name="LINE">
        <line class="cls-7" x1="966.83" y1="2570.62" x2="966.83" y2="2542.32" />
      </g>
      <g id="LINE-177" data-name="LINE">
        <line class="cls-7" x1="966.83" y1="2542.32" x2="1055.7" y2="2491.01" />
      </g>
      <g id="LINE-178" data-name="LINE">
        <line class="cls-7" x1="966.83" y1="2542.32" x2="843.92" y2="2471.36" />
      </g>
      <g id="LINE-179" data-name="LINE">
        <line class="cls-7" x1="1055.7" y1="2517.31" x2="1055.7" y2="2631.08" />
      </g>
      <g id="LINE-180" data-name="LINE">
        <line class="cls-7" x1="966.83" y1="2570.62" x2="966.83" y2="2682.39" />
      </g>
      <g id="LINE-181" data-name="LINE">
        <line class="cls-7" x1="629.52" y1="2525.87" x2="629.52" y2="2652.75" />
      </g>
      <g id="LINE-182" data-name="LINE">
        <line class="cls-7" x1="533.29" y1="2452.92" x2="533.29" y2="2597.2" />
      </g>
      <g id="LINE-183" data-name="LINE">
        <line class="cls-7" x1="629.52" y1="2480.85" x2="733.47" y2="2420.84" />
      </g>
      <g id="LINE-184" data-name="LINE">
        <polygon class="cls-8"
          points="1125 2443.7 1125 2477.3 1055.7 2517.32 1055.7 2491.01 932.79 2420.05 843.92 2471.36 843.92 2499.66 966.83 2570.61 905.23 2606.18 905.23 2557.86 823.85 2604.84 716.86 2543.07 716.86 2576.3 629.53 2525.88 733.47 2465.86 733.47 2420.84 637.24 2365.28 533.3 2425.3 533.3 2452.91 445.92 2402.47 513.05 2363.7 538.65 2378.49 580.59 2354.28 580.59 2317.39 659.32 2271.95 690.57 2289.99 765.74 2246.59 842.49 2290.89 880.31 2269.07 957.1 2313.39 985.65 2296.91 1069.27 2345.18 1069.27 2411.51 1125 2443.7" />
      </g>
      <g id="LINE-185" data-name="LINE">
        <line class="cls-7" x1="1055.7" y1="2631.08" x2="966.83" y2="2682.39" />
      </g>
      <g id="LINE-186" data-name="LINE">
        <line class="cls-7" x1="629.52" y1="2652.75" x2="533.29" y2="2597.2" />
      </g>
    </g>
    <g id="isla19">
      <g id="LINE-187" data-name="LINE">
        <polygon class="cls-8"
          points="8.79 2580.38 8.79 2559.6 0 2564.68 0 2508.93 22.84 2495.74 89.12 2534 8.79 2580.38" />
      </g>
    </g>
    <g id="isla20">
      <g class="cls-34">
        <image loading="lazy" data-clickable="true" data-category-name="el_club_de_futbol" width="202" height="175"
          transform="translate(280.73 2568.93) scale(2.23)" :href="image20" />
      </g>
      <g id="LINE-188" data-name="LINE">
        <path class="cls-1"
          d="M684.49,2803v-95.17C680.9,2653.32,598,2607,499.3,2604.45c-93.65-2.45-168.79,35.47-172.2,86.89v95.17l-.06,1c0,.13,0,.25,0,.38q-2.65,57.24,87.5,90.88,91.28,34.05,182.55,8.42T684.49,2803Zm-126-3.31a317.81,317.81,0,0,1-70.76.61l-95.25-55,85.18-49.18,130.1,75.11Z" />
      </g>
      <g id="ELLIPSE-3" data-name="ELLIPSE">
        <path class="cls-7"
          d="M684.43,2715c3.58-54.18-73.51-103.4-172.2-109.93s-181.6,32.1-185.18,86.29,73.51,103.4,172.19,109.93,181.6-32.1,185.19-86.29Z" />
      </g>
      <g id="ELLIPSE-4" data-name="ELLIPSE">
        <path class="cls-18" d="M327.05,2786.27c-.09,1.23-.13,2.46-.12,3.7" />
      </g>
      <g id="LINE-189" data-name="LINE">
        <line class="cls-7" x1="684.43" y1="2809.92" x2="684.43" y2="2707.84" />
      </g>
      <g id="LINE-190" data-name="LINE">
        <line class="cls-7" x1="558.46" y1="2799.7" x2="607.73" y2="2771.26" />
      </g>
      <g id="LINE-191" data-name="LINE">
        <line class="cls-7" x1="607.73" y1="2771.26" x2="477.63" y2="2696.14" />
      </g>
      <g id="LINE-192" data-name="LINE">
        <line class="cls-7" x1="477.63" y1="2696.14" x2="392.45" y2="2745.32" />
      </g>
      <g id="LINE-193" data-name="LINE">
        <line class="cls-7" x1="392.45" y1="2745.32" x2="487.7" y2="2800.31" />
      </g>
      <g id="SPLINE-7" data-name="SPLINE">
        <path class="cls-7" d="M327.05,2691.35v95.17" />
      </g>
      <g id="SPLINE-8" data-name="SPLINE">
        <path class="cls-7" d="M327.05,2786.52q-3.85,58.24,87.41,92.29T597,2887.24q91.28-25.63,87.42-84.22" />
      </g>
      <g id="SPLINE-9" data-name="SPLINE">
        <path class="cls-7" d="M684.43,2803q3.86,58.59-87.42,84.22t-182.55-8.43q-91.26-34-87.41-92.29" />
      </g>
    </g>
    <g id="isla21">
      <g class="cls-35">
        <image loading="lazy" data-clickable="true" data-category-name="el_teatro" width="93" height="123"
          transform="translate(69.07 2689.25) scale(2.23)" :href="image21" />
      </g>
      <g id="LINE-194" data-name="LINE">
        <polygon class="cls-1"
          points="246.02 2765.57 246.02 2877.81 159.86 2927.55 159.86 2839.77 91.74 2800.44 91.74 2775.99 177.9 2726.24 246.02 2765.57" />
      </g>
      <g id="LINE-195" data-name="LINE">
        <line class="cls-7" x1="246.02" y1="2877.91" x2="246.02" y2="2765.67" />
      </g>
      <g id="LINE-196" data-name="LINE">
        <line class="cls-7" x1="246.02" y1="2765.67" x2="177.9" y2="2726.34" />
      </g>
      <g id="LINE-197" data-name="LINE">
        <line class="cls-7" x1="177.9" y1="2726.34" x2="117.65" y2="2761.13" />
      </g>
      <g id="LINE-198" data-name="LINE">
        <line class="cls-7" x1="159.86" y1="2927.65" x2="159.86" y2="2839.87" />
      </g>
      <g id="LINE-199" data-name="LINE">
        <line class="cls-7" x1="91.74" y1="2776.09" x2="159.86" y2="2815.41" />
      </g>
      <g id="LINE-200" data-name="LINE">
        <line class="cls-7" x1="246.02" y1="2765.67" x2="159.86" y2="2815.41" />
      </g>
      <g id="LINE-201" data-name="LINE">
        <line class="cls-7" x1="159.86" y1="2815.41" x2="159.86" y2="2839.87" />
      </g>
      <g id="LINE-202" data-name="LINE">
        <polygon class="cls-8"
          points="72.72 2890.18 72.72 2803.61 0 2845.59 0 2696.22 13.77 2704.16 33.33 2692.87 65.63 2695.44 97.93 2730.16 97.93 2749.74 117.65 2761.13 91.74 2776.09 91.74 2800.55 159.86 2839.87 72.72 2890.18" />
      </g>
      <g id="LINE-203" data-name="LINE">
        <line class="cls-7" x1="159.86" y1="2927.65" x2="246.02" y2="2877.91" />
      </g>
    </g>
    <g id="isla22">
      <g class="cls-36">
        <g id="LINE-204" data-name="LINE">
          <polygon points="571.97 3034.57 341.36 3167.72 -0.01 3364.8 -0.01 3112.69 353.63 2908.52 571.97 3034.57" />
        </g>
      </g>
      <g class="cls-37">
        <image loading="lazy" data-clickable="true" data-category-name="el_huerto_urbano" width="124" height="107"
          transform="translate(115.86 3016.77) scale(2.23)" :href="image22" />
      </g>
      <g id="LINE-205" data-name="LINE">
        <polygon class="cls-1"
          points="341.36 3140.73 341.36 3167.66 281.95 3201.96 161.8 3132.59 161.8 3105.66 191.51 3080.09 221.21 3071.36 341.36 3140.73" />
      </g>
      <g>
        <g id="LINE-206" data-name="LINE">
          <line class="cls-5" x1="172.87" y1="3214.22" x2="220.88" y2="3186.5" />
        </g>
        <g id="LINE-207" data-name="LINE">
          <line class="cls-5" x1="220.88" y1="3186.5" x2="247.76" y2="3202.02" />
        </g>
        <g id="LINE-208" data-name="LINE">
          <line class="cls-5" x1="247.76" y1="3202.02" x2="199.75" y2="3229.74" />
        </g>
        <g id="LINE-209" data-name="LINE">
          <line class="cls-5" x1="199.75" y1="3229.74" x2="172.87" y2="3214.22" />
        </g>
        <g>
          <g id="ARC-46" data-name="ARC">
            <path class="cls-5" d="M471.45,2997.38A277.33,277.33,0,0,0,413.66,2964" />
          </g>
          <g id="ARC-47" data-name="ARC">
            <path class="cls-5" d="M493.87,3009.28a351,351,0,0,0-70,40.41" />
          </g>
          <g id="ARC-48" data-name="ARC">
            <path class="cls-5" d="M512.39,3020a351,351,0,0,0-70,40.41" />
          </g>
          <g id="ARC-49" data-name="ARC">
            <path class="cls-5" d="M530.91,3030.66a351,351,0,0,0-70,40.41" />
          </g>
          <g id="ARC-50" data-name="ARC">
            <path class="cls-5" d="M347.59,2983.68a184.39,184.39,0,0,0-43.88-25.34" />
          </g>
          <g id="ARC-51" data-name="ARC">
            <path class="cls-5" d="M363.88,2974.27A184.35,184.35,0,0,0,320,2948.94" />
          </g>
          <g id="ARC-52" data-name="ARC">
            <path class="cls-5" d="M380.92,2964.43a184.29,184.29,0,0,0-43.87-25.33" />
          </g>
          <g id="ARC-53" data-name="ARC">
            <path class="cls-5" d="M397.65,2954.77a184.29,184.29,0,0,0-43.87-25.33" />
          </g>
          <g id="ARC-54" data-name="ARC">
            <path class="cls-5" d="M454.72,3007a277.33,277.33,0,0,0-57.79-33.37" />
          </g>
          <g id="ARC-55" data-name="ARC">
            <path class="cls-5" d="M437.67,3016.88a277.47,277.47,0,0,0-57.78-33.36" />
          </g>
          <g id="ARC-56" data-name="ARC">
            <path class="cls-5" d="M421.38,3026.28a277.92,277.92,0,0,0-57.78-33.36" />
          </g>
          <g id="ARC-57" data-name="ARC">
            <path class="cls-5" d="M343.56,3080.71a133.66,133.66,0,0,0-42.17,24.35" />
          </g>
          <g id="ARC-58" data-name="ARC">
            <path class="cls-5" d="M362.46,3091.62A133.49,133.49,0,0,0,320.29,3116" />
          </g>
          <g id="ARC-59" data-name="ARC">
            <path class="cls-5" d="M382.1,3103a133.62,133.62,0,0,0-42.18,24.35" />
          </g>
          <g id="ARC-60" data-name="ARC">
            <path class="cls-5" d="M401.35,3114.08a133.43,133.43,0,0,0-42.18,24.35" />
          </g>
          <g id="ARC-61" data-name="ARC">
            <path class="cls-5" d="M430.91,3072a585.15,585.15,0,0,0-83.53-48.23" />
          </g>
          <g id="ARC-62" data-name="ARC">
            <path class="cls-5" d="M412.43,3082.66a585.5,585.5,0,0,0-83.53-48.22" />
          </g>
          <g id="ARC-63" data-name="ARC">
            <path class="cls-5" d="M394,3093.33a584.14,584.14,0,0,0-83.53-48.22" />
          </g>
          <g id="ARC-64" data-name="ARC">
            <path class="cls-5" d="M189.76,3077a179.57,179.57,0,0,0-49.22-28.42" />
          </g>
          <g id="ARC-65" data-name="ARC">
            <path class="cls-5" d="M209.27,3065.68a179.94,179.94,0,0,0-49.22-28.42" />
          </g>
          <g id="ARC-66" data-name="ARC">
            <path class="cls-5" d="M228.78,3054.42A179.43,179.43,0,0,0,179.56,3026" />
          </g>
          <g id="ARC-67" data-name="ARC">
            <path class="cls-5" d="M170.25,3088.21A179.7,179.7,0,0,0,121,3059.8" />
          </g>
          <g id="ARC-68" data-name="ARC">
            <path class="cls-5" d="M150.73,3099.48a179.68,179.68,0,0,0-49.22-28.42" />
          </g>
          <g id="ARC-69" data-name="ARC">
            <path class="cls-5" d="M341.47,3003.22a413.76,413.76,0,0,0-82.34,47.54" />
          </g>
          <g id="ARC-70" data-name="ARC">
            <path class="cls-5" d="M323,2992.53a413.76,413.76,0,0,0-82.34,47.54" />
          </g>
          <g id="ARC-71" data-name="ARC">
            <path class="cls-5" d="M304.43,2981.84a413.76,413.76,0,0,0-82.34,47.54" />
          </g>
          <g id="ARC-72" data-name="ARC">
            <path class="cls-5" d="M285.91,2971.15a413.76,413.76,0,0,0-82.34,47.54" />
          </g>
          <g id="ARC-73" data-name="ARC">
            <path class="cls-5" d="M205.75,3179.44a468.87,468.87,0,0,0-83.53-48.22" />
          </g>
          <g id="ARC-74" data-name="ARC">
            <path class="cls-5" d="M187.27,3190.11a469.79,469.79,0,0,0-83.52-48.23" />
          </g>
          <g id="ARC-75" data-name="ARC">
            <path class="cls-5" d="M168.8,3200.78a470.23,470.23,0,0,0-83.53-48.23" />
          </g>
          <g id="ARC-76" data-name="ARC">
            <path class="cls-5" d="M127.46,3193.22a466.84,466.84,0,0,0-70,40.41" />
          </g>
          <g id="ARC-77" data-name="ARC">
            <path class="cls-5" d="M108.94,3182.53a466.84,466.84,0,0,0-70,40.41" />
          </g>
          <g id="ARC-78" data-name="ARC">
            <path class="cls-5" d="M90.43,3171.84a465.85,465.85,0,0,0-70,40.41" />
          </g>
          <g id="ARC-79" data-name="ARC">
            <path class="cls-5" d="M71.91,3161.15a465.85,465.85,0,0,0-70,40.41" />
          </g>
          <g id="ARC-80" data-name="ARC">
            <path class="cls-5" d="M53.39,3150.46A465.84,465.84,0,0,0,0,3179.78" />
          </g>
          <g id="ARC-81" data-name="ARC">
            <path class="cls-5" d="M34.87,3139.77q-17.8,8.31-34.88,18.11" />
          </g>
          <g id="ARC-82" data-name="ARC">
            <path class="cls-5" d="M16.35,3129.07q-8.25,3.85-16.36,8" />
          </g>
          <g id="ARC-83" data-name="ARC">
            <path class="cls-5" d="M132.69,3274.64a291.74,291.74,0,0,0-57.78-33.36" />
          </g>
          <g id="ARC-84" data-name="ARC">
            <path class="cls-5" d="M151.17,3264a292.52,292.52,0,0,0-57.78-33.36" />
          </g>
          <g id="ARC-85" data-name="ARC">
            <path class="cls-5" d="M169.65,3253.3a292.59,292.59,0,0,0-57.79-33.36" />
          </g>
          <g id="ARC-86" data-name="ARC">
            <path class="cls-5" d="M188.12,3242.63a292.23,292.23,0,0,0-57.78-33.36" />
          </g>
          <g id="ARC-87" data-name="ARC">
            <path class="cls-5" d="M111.32,3281a176.45,176.45,0,0,0-50.07,28.9" />
          </g>
          <g id="ARC-88" data-name="ARC">
            <path class="cls-5" d="M92.84,3270.36a176.5,176.5,0,0,0-50.06,28.9" />
          </g>
          <g id="ARC-89" data-name="ARC">
            <path class="cls-5" d="M74.37,3259.69A176.34,176.34,0,0,0,24.3,3288.6" />
          </g>
          <g id="ARC-90" data-name="ARC">
            <path class="cls-5" d="M55.89,3249a176.58,176.58,0,0,0-50.07,28.91" />
          </g>
          <g id="ARC-91" data-name="ARC">
            <path class="cls-5" d="M37.41,3238.35A176.83,176.83,0,0,0,0,3257.78" />
          </g>
          <g id="ARC-92" data-name="ARC">
            <path class="cls-5" d="M18.93,3227.69A175.73,175.73,0,0,0,0,3236.1" />
          </g>
          <g id="ARC-93" data-name="ARC">
            <path class="cls-5" d="M37.88,3320.74A291.84,291.84,0,0,0,0,3296.91" />
          </g>
          <g id="ARC-94" data-name="ARC">
            <path class="cls-5" d="M18.37,3332q-9-6.63-18.38-12.56" />
          </g>
          <g id="LINE-210" data-name="LINE">
            <line class="cls-5" x1="278.86" y1="3095.51" x2="314.51" y2="3074.92" />
          </g>
          <g id="LINE-211" data-name="LINE">
            <line class="cls-5" x1="314.51" y1="3074.92" x2="287.03" y2="3059.05" />
          </g>
          <g id="LINE-212" data-name="LINE">
            <line class="cls-5" x1="287.03" y1="3059.05" x2="251.37" y2="3079.64" />
          </g>
          <g id="LINE-213" data-name="LINE">
            <line class="cls-5" x1="251.37" y1="3079.64" x2="278.86" y2="3095.51" />
          </g>
        </g>
      </g>
      <g id="ELLIPSE-5" data-name="ELLIPSE">
        <path class="cls-7"
          d="M104.69,3105.41c.57-8.6-11.67-16.41-27.33-17.45s-28.81,5.1-29.38,13.7,11.66,16.41,27.32,17.44,28.82-5.09,29.39-13.69Z" />
      </g>
      <g id="LINE-214" data-name="LINE">
        <line class="cls-7" x1="311.65" y1="3149.52" x2="191.5" y2="3080.15" />
      </g>
      <g id="LINE-215" data-name="LINE">
        <line class="cls-7" x1="341.36" y1="3140.79" x2="311.65" y2="3149.52" />
      </g>
      <g id="LINE-216" data-name="LINE">
        <line class="cls-7" x1="311.65" y1="3149.52" x2="281.95" y2="3175.09" />
      </g>
      <g id="LINE-217" data-name="LINE">
        <line class="cls-7" x1="281.95" y1="3175.09" x2="161.8" y2="3105.72" />
      </g>
      <g id="LINE-218" data-name="LINE">
        <line class="cls-7" x1="281.95" y1="3175.09" x2="281.95" y2="3202.02" />
      </g>
      <g id="LINE-219" data-name="LINE">
        <line class="cls-7" x1="281.95" y1="3202.02" x2="161.8" y2="3132.65" />
      </g>
      <g id="LINE-220" data-name="LINE">
        <line class="cls-7" x1="161.8" y1="3132.65" x2="161.8" y2="3105.72" />
      </g>
      <g id="LINE-221" data-name="LINE">
        <line class="cls-7" x1="161.8" y1="3105.72" x2="191.5" y2="3080.15" />
      </g>
      <g id="LINE-222" data-name="LINE">
        <line class="cls-7" x1="191.5" y1="3080.15" x2="221.21" y2="3071.42" />
      </g>
      <g id="LINE-223" data-name="LINE">
        <line class="cls-7" x1="221.21" y1="3071.42" x2="341.36" y2="3140.79" />
      </g>
      <g id="LINE-224" data-name="LINE">
        <line class="cls-7" x1="341.36" y1="3140.79" x2="341.36" y2="3167.72" />
      </g>
      <g id="SPLINE-10" data-name="SPLINE">
        <path class="cls-7" d="M48,3114.88q-1,15.15,26.56,17.39t30.06-12.8" />
      </g>
      <g id="SPLINE-11" data-name="SPLINE">
        <path class="cls-7" d="M104.63,3119.47l.08-14.45" />
      </g>
      <g id="LWPOLYLINE-14" data-name="LWPOLYLINE">
        <line class="cls-7" x1="281.95" y1="3202.02" x2="341.36" y2="3167.72" />
      </g>
      <g id="LWPOLYLINE-15" data-name="LWPOLYLINE">
        <line class="cls-7" x1="48.01" y1="3114.88" x2="48.01" y2="3103.22" />
      </g>
    </g>
    <g id="isla23">
      <g class="cls-38">
        <image loading="lazy" data-clickable="true" data-category-name="el_rio" width="1129" height="899"
          transform="translate(-4 2731)" :href="image23" />
      </g>
      <g id="LINE-225" data-name="LINE">
        <polygon class="cls-7" points="1125 2739.47 1125 2960.07 0 3609.59 0 3388.99 1125 2739.47" />
      </g>
    </g>
    <g id="isla24">
      <g id="LINE-226" data-name="LINE">
        <polygon class="cls-8"
          points="1125 2989.22 1125 3165.13 1081.14 3139.8 1081.14 3197.89 1023.02 3164.33 1023.02 3116.18 950.1 3074.08 1008.32 3040.47 1041.01 3059.34 1071.73 3041.61 1071.73 3019.98 1125 2989.22" />
      </g>
    </g>
    <g id="isla25">
      <g id="el_tribunal">
        <g class="el_tribunal__image">
          <image loading="lazy" data-clickable="true" data-category-name="el_tribunal" width="100" height="113"
            transform="translate(1115.5 3639.83) rotate(180) scale(2.23)" :href="image48" />
        </g>
      </g>
      <g class="cls-39">
        <image loading="lazy" data-clickable="true" data-category-name="los_bomberos" width="113" height="144"
          transform="translate(579.29 3172.73) scale(2.23)" :href="image24" />
      </g>
      <g id="LINE-227" data-name="LINE">
        <polygon class="cls-1"
          points="1102.71 3474.49 1102.71 3570.15 1017.18 3619.53 901.72 3552.87 901.72 3457.21 987.26 3407.83 1044.98 3414.05 1102.71 3474.49" />
      </g>
      <g id="LINE-228" data-name="LINE">
        <polygon class="cls-1"
          points="791.42 3271.39 791.42 3311.45 717.52 3354.11 717.52 3446.31 628.78 3395.07 628.78 3262.82 702.67 3220.15 702.68 3220.15 791.42 3271.39" />
      </g>
      <g id="LINE-229" data-name="LINE">
        <line class="cls-7" x1="1017.18" y1="3619.16" x2="1017.18" y2="3523.5" />
      </g>
      <g id="LINE-230" data-name="LINE">
        <line class="cls-7" x1="628.81" y1="3394.94" x2="628.81" y2="3262.68" />
      </g>
      <g id="LINE-231" data-name="LINE">
        <line class="cls-7" x1="628.81" y1="3262.68" x2="717.55" y2="3313.92" />
      </g>
      <g id="LINE-232" data-name="LINE">
        <line class="cls-7" x1="717.55" y1="3313.92" x2="717.55" y2="3353.98" />
      </g>
      <g id="LINE-233" data-name="LINE">
        <line class="cls-7" x1="901.73" y1="3456.84" x2="901.73" y2="3552.51" />
      </g>
      <g id="LINE-234" data-name="LINE">
        <polygon class="cls-8"
          points="1124.99 3240.78 1124.99 3408.92 1102.71 3421.79 1102.71 3474.11 1044.98 3413.68 987.25 3407.46 901.73 3456.84 901.73 3414.29 803.43 3357.54 803.43 3403.56 717.55 3353.98 791.45 3311.31 791.45 3271.25 733.84 3237.99 757.02 3224.59 757.02 3212.27 812.83 3180.05 812.83 3156 865.46 3125.62 981.95 3192.88 981.95 3215.29 1053.95 3256.87 1085.98 3238.38 1124.99 3240.78" />
      </g>
      <g id="LINE-235" data-name="LINE">
        <line class="cls-7" x1="1102.71" y1="3474.12" x2="1102.71" y2="3569.78" />
      </g>
      <g id="LINE-236" data-name="LINE">
        <line class="cls-7" x1="628.81" y1="3262.68" x2="703.06" y2="3219.81" />
      </g>
      <g id="LINE-237" data-name="LINE">
        <line class="cls-7" x1="717.55" y1="3446.17" x2="717.55" y2="3353.98" />
      </g>
      <g id="LINE-238" data-name="LINE">
        <line class="cls-7" x1="791.45" y1="3271.25" x2="717.55" y2="3313.92" />
      </g>
      <g id="LINE-239" data-name="LINE">
        <line class="cls-7" x1="1044.99" y1="3413.68" x2="959.45" y2="3463.06" />
      </g>
      <g id="LINE-240" data-name="LINE">
        <line class="cls-7" x1="959.45" y1="3463.06" x2="1017.18" y2="3523.5" />
      </g>
      <g id="LINE-241" data-name="LINE">
        <line class="cls-7" x1="1017.18" y1="3523.5" x2="1102.71" y2="3474.12" />
      </g>
      <g id="LINE-242" data-name="LINE">
        <line class="cls-7" x1="901.73" y1="3456.84" x2="959.45" y2="3463.06" />
      </g>
      <g id="LWPOLYLINE-16" data-name="LWPOLYLINE">
        <line class="cls-7" x1="628.81" y1="3394.94" x2="717.55" y2="3446.17" />
      </g>
      <g id="LWPOLYLINE-17" data-name="LWPOLYLINE">
        <line class="cls-7" x1="901.73" y1="3552.51" x2="1017.18" y2="3619.16" />
      </g>
      <g id="LWPOLYLINE-18" data-name="LWPOLYLINE">
        <line class="cls-7" x1="1017.18" y1="3619.16" x2="1102.71" y2="3569.78" />
      </g>
      <g id="LWPOLYLINE-19" data-name="LWPOLYLINE">
        <line class="cls-7" x1="733.83" y1="3237.99" x2="703.06" y2="3219.81" />
      </g>
    </g>
    <g id="isla26">
      <g class="cls-40">
        <image loading="lazy" data-clickable="true" data-category-name="la_discoteca" width="110" height="134"
          transform="translate(249.54 3399.99) scale(2.23)" :href="image25" />
      </g>
      <g id="LINE-243" data-name="LINE">
        <polygon class="cls-1"
          points="449.99 3484.29 449.99 3518.77 377.83 3560.44 377.83 3639.57 291.47 3589.71 291.47 3476.09 363.63 3434.43 449.99 3484.29" />
      </g>
      <g id="LINE-244" data-name="LINE">
        <line class="cls-7" x1="291.47" y1="3589.71" x2="291.47" y2="3476.09" />
      </g>
      <g id="LINE-245" data-name="LINE">
        <polygon class="cls-8"
          points="789.45 3445.07 716.53 3487.17 716.53 3535.32 658.41 3568.87 658.41 3510.79 598.08 3545.62 598.08 3582.38 532.43 3620.29 461.62 3579.4 461.62 3608.82 377.83 3560.44 449.99 3518.78 449.99 3484.29 392.8 3451.27 404.05 3444.78 404.05 3400.06 481.79 3355.18 509.2 3371 548.49 3348.31 584.55 3369.13 607.27 3356.01 667.82 3390.97 667.82 3412.6 698.54 3430.33 731.23 3411.45 789.45 3445.07" />
      </g>
      <g id="LINE-246" data-name="LINE">
        <line class="cls-7" x1="377.83" y1="3560.44" x2="377.83" y2="3525.95" />
      </g>
      <g id="LINE-247" data-name="LINE">
        <line class="cls-7" x1="377.83" y1="3639.57" x2="377.83" y2="3560.44" />
      </g>
      <g id="LINE-248" data-name="LINE">
        <line class="cls-7" x1="291.47" y1="3476.09" x2="377.83" y2="3525.95" />
      </g>
      <g id="LINE-249" data-name="LINE">
        <line class="cls-7" x1="377.83" y1="3525.95" x2="449.99" y2="3484.29" />
      </g>
      <g id="LINE-250" data-name="LINE">
        <line class="cls-7" x1="363.63" y1="3434.43" x2="291.47" y2="3476.09" />
      </g>
      <g id="LWPOLYLINE-20" data-name="LWPOLYLINE">
        <line class="cls-7" x1="377.83" y1="3639.57" x2="291.47" y2="3589.71" />
      </g>
      <g id="LWPOLYLINE-21" data-name="LWPOLYLINE">
        <line class="cls-7" x1="392.79" y1="3451.27" x2="363.63" y2="3434.43" />
      </g>
    </g>
    <g id="isla27">
      <g class="cls-41">
        <image loading="lazy" data-clickable="true" data-category-name="el_parlamento" width="144" height="163"
          transform="translate(11.14 3609.43) scale(2.23)" :href="image26" />
      </g>
      <g id="LINE-251" data-name="LINE">
        <polygon class="cls-1"
          points="262.05 3742.41 262.05 3884.9 171.58 3937.13 171.58 3821.43 39.37 3745.1 39.37 3718.31 84.51 3665.36 129.74 3665.36 262.05 3742.41" />
      </g>
      <g id="LINE-252" data-name="LINE">
        <line class="cls-18" x1="452.11" y1="3674.9" x2="452.1" y2="3674.9" />
      </g>
      <g id="LINE-253" data-name="LINE">
        <polygon class="cls-8"
          points="452.1 3674.9 421.09 3674.9 390.07 3710.72 390.07 3681.16 328.05 3716.98 328.05 3763.63 262.09 3801.71 262.09 3742.41 129.79 3665.36 84.55 3665.36 39.42 3718.32 39.42 3745.1 171.63 3821.43 83.15 3872.51 83.15 3911.9 10.97 3953.57 10.97 3929.67 -0.01 3936.01 -0.01 3657.08 27.04 3641.47 27.04 3603.42 100.14 3561.21 117.87 3571.44 155.64 3533.54 211.14 3525.14 282.73 3566.47 299.48 3556.8 387.83 3607.81 387.83 3637.79 452.1 3674.9" />
      </g>
      <g>
        <g id="LINE-254" data-name="LINE">
          <line class="cls-7" x1="262.1" y1="3801.71" x2="262.1" y2="3884.9" />
        </g>
        <g id="LINE-255" data-name="LINE">
          <line class="cls-7" x1="171.63" y1="3821.43" x2="171.63" y2="3794.65" />
        </g>
        <g id="LINE-256" data-name="LINE">
          <line class="cls-7" x1="216.86" y1="3742.41" x2="262.1" y2="3742.41" />
        </g>
        <g id="LINE-257" data-name="LINE">
          <line class="cls-7" x1="171.63" y1="3937.13" x2="171.63" y2="3821.43" />
        </g>
        <g id="LINE-258" data-name="LINE">
          <line class="cls-7" x1="84.56" y1="3665.36" x2="216.86" y2="3742.41" />
        </g>
        <g id="LINE-259" data-name="LINE">
          <line class="cls-7" x1="216.86" y1="3742.41" x2="171.63" y2="3794.65" />
        </g>
        <g id="LINE-260" data-name="LINE">
          <line class="cls-7" x1="171.63" y1="3794.65" x2="39.42" y2="3718.31" />
        </g>
        <g id="LWPOLYLINE-22" data-name="LWPOLYLINE">
          <line class="cls-7" x1="171.63" y1="3937.13" x2="262.1" y2="3884.9" />
        </g>
      </g>
    </g>
    <g id="isla28">
      <g class="cls-42">
        <image loading="lazy" data-clickable="true" data-category-name="el_supermercado" width="158" height="181"
          transform="translate(672.87 3569.32) scale(2.23)" :href="image27" />
      </g>
      <g id="LINE-261" data-name="LINE">
        <polygon class="cls-8"
          points="1125 3646.46 1125 3994.06 1072.44 3939.03 1014.71 3932.81 1014.71 3890.25 916.42 3833.51 916.42 3879.53 830.54 3829.94 904.44 3787.28 904.44 3747.22 867.36 3725.81 885.94 3715.09 885.94 3679.04 917.46 3646.45 948.99 3642.64 948.99 3618.59 1012.86 3581.71 1125 3646.46" />
      </g>
      <g>
        <g id="LINE-262" data-name="LINE">
          <line class="cls-7" x1="741.79" y1="3738.65" x2="815.69" y2="3695.98" />
        </g>
        <g id="LINE-263" data-name="LINE">
          <line class="cls-7" x1="815.69" y1="3695.98" x2="867.35" y2="3725.81" />
        </g>
        <g id="LINE-264" data-name="LINE">
          <line class="cls-7" x1="830.54" y1="3922.14" x2="830.54" y2="3829.95" />
        </g>
        <g id="LINE-265" data-name="LINE">
          <line class="cls-7" x1="904.43" y1="3747.22" x2="830.54" y2="3789.88" />
        </g>
        <g id="LINE-266" data-name="LINE">
          <line class="cls-7" x1="741.79" y1="3870.9" x2="741.79" y2="3738.65" />
        </g>
        <g id="LINE-267" data-name="LINE">
          <line class="cls-7" x1="741.79" y1="3738.65" x2="830.54" y2="3789.88" />
        </g>
        <g id="LINE-268" data-name="LINE">
          <line class="cls-7" x1="830.54" y1="3789.88" x2="830.54" y2="3829.95" />
        </g>
        <g id="LWPOLYLINE-23" data-name="LWPOLYLINE">
          <line class="cls-7" x1="830.54" y1="3922.14" x2="741.79" y2="3870.9" />
        </g>
      </g>
      <g id="LINE-269" data-name="LINE">
        <polygon class="cls-1"
          points="904.43 3747.21 904.43 3787.28 830.53 3829.94 830.53 3922.13 741.79 3870.9 741.79 3738.64 815.69 3695.98 867.35 3725.81 904.43 3747.21" />
      </g>
    </g>
    <g id="isla29">
      <g class="cls-43">
        <image loading="lazy" data-clickable="true" data-category-name="la_empresa" width="90" height="119"
          transform="translate(802.1 3972.6) scale(2.23)" :href="image28" />
      </g>
      <g id="LINE-270" data-name="LINE">
        <polygon class="cls-8"
          points="1049.85 4050.09 1018.83 4050.09 987.81 4085.9 987.81 4034.83 903.86 3986.36 815.4 4037.44 815.4 4064.22 899.35 4112.69 854.11 4112.69 808.88 4164.92 676.67 4088.59 676.67 4134.98 590.73 4085.36 590.73 4057.9 427.68 3963.76 550.48 3892.86 550.48 3870.42 605.97 3814.74 661.47 3806.34 733.07 3847.67 749.82 3838 838.16 3889.01 838.16 3935.67 888.79 3964.9 918.5 3947.75 986.93 3987.26 986.93 4013.76 1049.85 4050.09" />
      </g>
      <g class="cls-44">
        <image loading="lazy" data-clickable="true" data-category-name="el_observatorio" width="169" height="134"
          transform="translate(493 3885)" :href="image29" />
      </g>
      <g id="SPLINE-12" data-name="SPLINE">
        <path class="cls-7" d="M504.17,3967.27q-2.64,40,70.17,44.8t75.46-35.16" />
      </g>
      <g id="SPLINE-13" data-name="SPLINE">
        <path class="cls-7" d="M649.8,3976.91q6.13-44.19-30.34-69.88t-76-5q-39.54,20.65-39.28,65.27" />
      </g>
      <g>
        <g id="LINE-271" data-name="LINE">
          <line class="cls-7" x1="899.35" y1="4228.39" x2="899.35" y2="4112.69" />
        </g>
        <g id="LINE-272" data-name="LINE">
          <line class="cls-7" x1="987.81" y1="4085.9" x2="987.81" y2="4177.31" />
        </g>
        <g id="LINE-273" data-name="LINE">
          <line class="cls-7" x1="815.4" y1="4037.44" x2="899.35" y2="4085.91" />
        </g>
        <g id="LINE-274" data-name="LINE">
          <line class="cls-7" x1="899.35" y1="4085.91" x2="987.81" y2="4034.83" />
        </g>
        <g id="LWPOLYLINE-24" data-name="LWPOLYLINE">
          <line class="cls-7" x1="899.35" y1="4085.91" x2="899.35" y2="4112.69" />
        </g>
        <g id="LWPOLYLINE-25" data-name="LWPOLYLINE">
          <line class="cls-7" x1="899.35" y1="4228.39" x2="987.81" y2="4177.31" />
        </g>
      </g>
    </g>
    <g id="isla30">
      <g class="la_television__image">
        <image loading="lazy" data-clickable="true" data-category-name="la_television" width="101" height="117"
          transform="translate(321.48 4247.3) scale(2.23)" :href="image49" />
      </g>
      <g class="cls-45">
        <image loading="lazy" data-clickable="true" data-category-name="el_manicomio" width="136" height="152"
          transform="translate(-3.11 4040.38) scale(2.23)" :href="image30" />
      </g>
      <g class="cls-46">
        <image loading="lazy" data-clickable="true" data-category-name="una_comunidad" width="80" height="114"
          transform="translate(570.38 4124.11) scale(2.23)" :href="image31" />
      </g>
      <g id="LINE-275" data-name="LINE">
        <polygon class="cls-8"
          points="661.78 4247.47 599.63 4283.35 599.63 4304.35 532.63 4343.05 532.63 4323.03 447.08 4273.65 407.35 4272.57 367.62 4319.52 367.62 4301.85 296.04 4260.53 296.04 4308.91 225.27 4268.06 225.27 4243.68 158.76 4205.27 235.24 4161.13 235.24 4138.65 164.27 4097.69 221.06 4064.91 221.06 4041.49 277.31 4009.03 320.62 4034.03 340.19 4022.74 372.49 4025.32 404.78 4060.03 404.78 4079.61 424.51 4090.99 484.76 4056.22 552.88 4095.55 552.88 4122.68 620.65 4161.81 585.16 4182.31 585.16 4203.23 661.78 4247.47" />
      </g>
      <g data-clickable="true" data-category-name="la_estacion">
        <g id="LINE-276" data-name="LINE">
          <line class="cls-7" x1="532.63" y1="4343.05" x2="532.63" y2="4440.11" />
        </g>
        <g id="LINE-277" data-name="LINE">
          <line class="cls-7" x1="492.9" y1="4321.97" x2="453.17" y2="4368.91" />
        </g>
        <g id="LINE-278" data-name="LINE">
          <line class="cls-7" x1="367.63" y1="4319.52" x2="453.17" y2="4368.91" />
        </g>
        <g id="LINE-279" data-name="LINE">
          <line class="cls-7" x1="453.17" y1="4368.91" x2="453.17" y2="4485.99" />
        </g>
        <g id="LINE-280" data-name="LINE">
          <line class="cls-7" x1="492.9" y1="4321.97" x2="532.63" y2="4323.03" />
        </g>
        <g id="LINE-281" data-name="LINE">
          <line class="cls-7" x1="407.35" y1="4272.58" x2="492.9" y2="4321.97" />
        </g>
        <g id="LINE-282" data-name="LINE">
          <line class="cls-7" x1="367.63" y1="4436.6" x2="367.63" y2="4319.52" />
        </g>
        <g id="LWPOLYLINE-26" data-name="LWPOLYLINE">
          <line class="cls-7" x1="532.63" y1="4440.11" x2="453.17" y2="4485.99" />
        </g>
        <g id="LWPOLYLINE-27" data-name="LWPOLYLINE">
          <line class="cls-7" x1="453.17" y1="4485.99" x2="367.63" y2="4436.6" />
        </g>
      </g>
      <g>
        <g id="LINE-283" data-name="LINE">
          <line class="cls-7" x1="64.81" y1="4128.56" x2="158.77" y2="4182.81" />
        </g>
        <g id="LINE-284" data-name="LINE">
          <line class="cls-7" x1="158.77" y1="4182.81" x2="158.77" y2="4316.01" />
        </g>
        <g id="LINE-285" data-name="LINE">
          <line class="cls-7" x1="64.81" y1="4261.76" x2="64.81" y2="4128.56" />
        </g>
        <g id="LINE-286" data-name="LINE">
          <line class="cls-7" x1="64.81" y1="4128.56" x2="141.28" y2="4084.41" />
        </g>
        <g id="LINE-287" data-name="LINE">
          <line class="cls-7" x1="235.24" y1="4138.66" x2="158.77" y2="4182.81" />
        </g>
        <g id="LWPOLYLINE-28" data-name="LWPOLYLINE">
          <line class="cls-7" x1="158.77" y1="4316.01" x2="64.81" y2="4261.76" />
        </g>
        <g id="LWPOLYLINE-29" data-name="LWPOLYLINE">
          <line class="cls-7" x1="164.28" y1="4097.69" x2="141.28" y2="4084.41" />
        </g>
      </g>
      <g>
        <g id="LINE-288" data-name="LINE">
          <line class="cls-7" x1="728.56" y1="4187.99" x2="728.56" y2="4305.14" />
        </g>
        <g id="LINE-289" data-name="LINE">
          <line class="cls-7" x1="661.79" y1="4226.54" x2="661.79" y2="4247.46" />
        </g>
        <g id="LINE-290" data-name="LINE">
          <line class="cls-7" x1="661.79" y1="4365.55" x2="661.79" y2="4247.46" />
        </g>
        <g id="LINE-291" data-name="LINE">
          <line class="cls-7" x1="585.16" y1="4182.3" x2="661.79" y2="4226.54" />
        </g>
        <g id="LINE-292" data-name="LINE">
          <line class="cls-7" x1="661.79" y1="4226.54" x2="728.56" y2="4187.99" />
        </g>
        <g id="LINE-293" data-name="LINE">
          <line class="cls-7" x1="728.56" y1="4187.99" x2="651.93" y2="4143.75" />
        </g>
        <g id="LWPOLYLINE-30" data-name="LWPOLYLINE">
          <polyline class="cls-7" points="675.64 4357.55 675.64 4335.69 728.56 4305.14" />
        </g>
        <g id="LWPOLYLINE-31" data-name="LWPOLYLINE">
          <line class="cls-7" x1="675.64" y1="4357.55" x2="661.79" y2="4365.55" />
        </g>
        <g id="LWPOLYLINE-32" data-name="LWPOLYLINE">
          <line class="cls-7" x1="620.65" y1="4161.81" x2="651.93" y2="4143.75" />
        </g>
      </g>
    </g>
    <g id="isla31">
      <g class="cls-47">
        <image loading="lazy" data-clickable="true" data-category-name="la_policia" width="150" height="154"
          transform="translate(773.13 4304.58) scale(2.23)" :href="image32" />
      </g>
      <g id="LINE-294" data-name="LINE">
        <polygon class="cls-8"
          points="1125 4227.77 1125 4508.81 1103.74 4511.04 1064.01 4552.73 998.75 4515.06 998.75 4550.13 932.53 4511.89 1024.48 4458.81 1024.48 4431.62 981.72 4385.01 938.96 4382.24 847 4435.34 847 4400.65 769.6 4355.98 769.6 4389.94 675.64 4335.69 752.11 4291.54 769.01 4301.3 817.97 4273.02 817.97 4192.94 876.1 4159.39 903.93 4175.44 945.37 4151.52 973.94 4168.02 1005.9 4149.58 1070.5 4186.87 1070.5 4236.45 1090.22 4247.85 1125 4227.77" />
      </g>
      <g>
        <g id="LINE-295" data-name="LINE">
          <line class="cls-7" x1="847" y1="4549.23" x2="847" y2="4435.33" />
        </g>
        <g id="LINE-296" data-name="LINE">
          <line class="cls-7" x1="932.53" y1="4484.71" x2="889.77" y2="4438.1" />
        </g>
        <g id="LINE-297" data-name="LINE">
          <line class="cls-7" x1="889.77" y1="4438.1" x2="981.72" y2="4385.01" />
        </g>
        <g id="LINE-298" data-name="LINE">
          <line class="cls-7" x1="889.77" y1="4438.1" x2="847" y2="4435.33" />
        </g>
        <g id="LINE-299" data-name="LINE">
          <line class="cls-7" x1="932.53" y1="4511.89" x2="932.53" y2="4484.71" />
        </g>
        <g id="LINE-300" data-name="LINE">
          <line class="cls-7" x1="932.53" y1="4484.71" x2="1024.48" y2="4431.62" />
        </g>
        <g id="LINE-301" data-name="LINE">
          <line class="cls-7" x1="932.53" y1="4511.89" x2="932.53" y2="4598.61" />
        </g>
        <g id="LWPOLYLINE-33" data-name="LWPOLYLINE">
          <line class="cls-7" x1="932.53" y1="4598.61" x2="847" y2="4549.23" />
        </g>
      </g>
    </g>
    <g id="isla35">
      <g class="la_estacion__image">
        <image loading="lazy" data-clickable="true" data-category-name="la_estacion" width="93" height="123"
          transform="translate(939.43 4598.59) rotate(90) scale(2.23)" :href="image50" />
      </g>
      <g>
        <g id="LINE-302" data-name="LINE">
          <line class="cls-5" x1="-0.93" y1="4397.45" x2="631.08" y2="4762.34" />
        </g>
        <g id="LINE-303" data-name="LINE">
          <line class="cls-5" x1="679.98" y1="4790.57" x2="1124.08" y2="5046.97" />
        </g>
        <g id="LINE-304" data-name="LINE">
          <line class="cls-5" x1="-0.93" y1="4377.17" x2="648.65" y2="4752.2" />
        </g>
        <g id="LINE-305" data-name="LINE">
          <line class="cls-5" x1="679.98" y1="4770.29" x2="1124.08" y2="5026.69" />
        </g>
        <g id="LINE-306" data-name="LINE">
          <line class="cls-5" x1="-0.93" y1="4349.69" x2="672.44" y2="4738.46" />
        </g>
        <g id="LINE-307" data-name="LINE">
          <line class="cls-5" x1="679.98" y1="4742.81" x2="1124.08" y2="4999.21" />
        </g>
        <g id="LINE-308" data-name="LINE">
          <line class="cls-5" x1="-0.93" y1="4329.41" x2="1124.08" y2="4978.93" />
        </g>
        <g id="LWPOLYLINE-34" data-name="LWPOLYLINE">
          <line class="cls-7" x1="679.98" y1="4734.11" x2="679.98" y2="4790.57" />
        </g>
        <g id="LWPOLYLINE-35" data-name="LWPOLYLINE">
          <line class="cls-7" x1="679.98" y1="4734.11" x2="631.08" y2="4762.34" />
        </g>
      </g>
      <g>
        <g id="LINE-309" data-name="LINE">
          <line class="cls-7" x1="854.53" y1="4777.93" x2="854.53" y2="4740.83" />
        </g>
        <g id="LINE-310" data-name="LINE">
          <line class="cls-7" x1="931.11" y1="4696.61" x2="931.11" y2="4733.71" />
        </g>
        <g id="LINE-311" data-name="LINE">
          <line class="cls-7" x1="854.53" y1="4740.83" x2="690.75" y2="4646.27" />
        </g>
        <g id="LINE-312" data-name="LINE">
          <line class="cls-7" x1="690.75" y1="4683.37" x2="690.75" y2="4646.27" />
        </g>
        <g id="LINE-313" data-name="LINE">
          <line class="cls-7" x1="854.53" y1="4740.83" x2="931.11" y2="4696.61" />
        </g>
        <g id="LINE-314" data-name="LINE">
          <line class="cls-7" x1="931.11" y1="4696.61" x2="767.34" y2="4602.06" />
        </g>
        <g id="LINE-315" data-name="LINE">
          <line class="cls-7" x1="767.34" y1="4602.06" x2="690.75" y2="4646.27" />
        </g>
        <g id="LWPOLYLINE-36" data-name="LWPOLYLINE">
          <polyline class="cls-7" points="931.11 4733.71 854.53 4777.93 690.75 4683.37" />
        </g>
      </g>
    </g>
    <g id="isla32">
      <g class="cls-48">
        <image loading="lazy" data-clickable="true" data-category-name="la_asociacion_cannabica" width="158" height="135"
          transform="translate(-91.47 4431.78) scale(2.23)" :href="image33" />
      </g>
      <g id="LINE-316" data-name="LINE">
        <polygon class="cls-8"
          points="131.88 4554.05 63.7 4593.42 63.7 4612.23 -0.01 4649.01 -0.01 4400.5 5.76 4397.17 62.72 4430.05 62.72 4465.3 88.92 4480.43 64.83 4494.34 64.83 4515.34 131.88 4554.05" />
      </g>
      <g>
        <g id="LINE-317" data-name="LINE">
          <line class="cls-7" x1="212.21" y1="4625.11" x2="212.21" y2="4486.67" />
        </g>
        <g id="LINE-318" data-name="LINE">
          <line class="cls-7" x1="212.21" y1="4486.67" x2="145.17" y2="4447.96" />
        </g>
        <g id="LINE-319" data-name="LINE">
          <line class="cls-7" x1="131.88" y1="4671.49" x2="131.88" y2="4554.05" />
        </g>
        <g id="LINE-320" data-name="LINE">
          <line class="cls-7" x1="64.84" y1="4494.34" x2="131.88" y2="4533.05" />
        </g>
        <g id="LINE-321" data-name="LINE">
          <line class="cls-7" x1="131.88" y1="4533.05" x2="212.21" y2="4486.67" />
        </g>
        <g id="LWPOLYLINE-37" data-name="LWPOLYLINE">
          <line class="cls-7" x1="131.88" y1="4671.49" x2="212.21" y2="4625.11" />
        </g>
        <g id="LWPOLYLINE-38" data-name="LWPOLYLINE">
          <line class="cls-7" x1="131.88" y1="4554.05" x2="131.88" y2="4533.05" />
        </g>
        <g id="LWPOLYLINE-39" data-name="LWPOLYLINE">
          <line class="cls-7" x1="88.93" y1="4480.43" x2="145.17" y2="4447.96" />
        </g>
      </g>
    </g>
    <g id="isla33">
      <g class="cls-49">
        <image loading="lazy" data-clickable="true" data-category-name="el_restaurante" width="96" height="123"
          transform="translate(360.29 4770.06) scale(2.23)" :href="image34" />
      </g>
      <g class="cls-50">
        <image loading="lazy" data-clickable="true" data-category-name="la_carcel" width="88" height="112"
          transform="translate(73.53 4687.8) scale(2.23)" :href="image35" />
      </g>
      <g id="LINE-322" data-name="LINE">
        <polygon class="cls-8"
          points="680.9 4734.14 606.77 4776.93 606.77 4845.2 539.78 4883.88 539.78 4840.44 459.08 4793.85 394.96 4830.87 394.96 4876.6 475.67 4923.2 405.51 4963.7 334.56 4922.73 334.56 4902.2 290.37 4858.25 246.16 4851.15 246.16 4877.85 178.29 4838.67 254.75 4794.53 254.75 4752.31 161.91 4698.71 85.45 4742.86 85.45 4770.6 17.14 4731.16 126.95 4667.76 149.94 4681.04 185.25 4660.66 185.25 4620.8 239.88 4589.26 265.64 4604.13 292.54 4588.6 337.43 4614.52 359.86 4601.57 399.01 4602.85 438.18 4646.79 438.18 4681.89 457.43 4693 506.49 4664.67 568.45 4700.45 595.5 4684.83 680.9 4734.14" />
      </g>
      <g>
        <g id="LINE-323" data-name="LINE">
          <line class="cls-7" x1="539.79" y1="4883.88" x2="539.79" y2="4970.81" />
        </g>
        <g id="LINE-324" data-name="LINE">
          <line class="cls-7" x1="394.96" y1="4830.87" x2="475.67" y2="4877.46" />
        </g>
        <g id="LINE-325" data-name="LINE">
          <line class="cls-7" x1="475.67" y1="5014.2" x2="475.67" y2="4877.46" />
        </g>
        <g id="LINE-326" data-name="LINE">
          <line class="cls-7" x1="475.67" y1="4877.46" x2="539.79" y2="4840.44" />
        </g>
        <g id="LWPOLYLINE-40" data-name="LWPOLYLINE">
          <line class="cls-7" x1="485.84" y1="5001.96" x2="539.79" y2="4970.81" />
        </g>
        <g id="LWPOLYLINE-41" data-name="LWPOLYLINE">
          <line class="cls-7" x1="485.84" y1="5001.96" x2="485.84" y2="5008.33" />
        </g>
        <g id="LWPOLYLINE-42" data-name="LWPOLYLINE">
          <line class="cls-7" x1="475.67" y1="5014.2" x2="485.84" y2="5008.33" />
        </g>
      </g>
      <g>
        <g id="LINE-327" data-name="LINE">
          <line class="cls-7" x1="85.45" y1="4770.6" x2="85.45" y2="4869.91" />
        </g>
        <g id="LINE-328" data-name="LINE">
          <line class="cls-7" x1="85.45" y1="4742.86" x2="178.29" y2="4796.46" />
        </g>
        <g id="LINE-329" data-name="LINE">
          <line class="cls-7" x1="254.75" y1="4752.32" x2="178.29" y2="4796.46" />
        </g>
        <g id="LINE-330" data-name="LINE">
          <line class="cls-7" x1="178.29" y1="4796.46" x2="178.29" y2="4923.51" />
        </g>
        <g id="LWPOLYLINE-43" data-name="LWPOLYLINE">
          <line class="cls-7" x1="178.29" y1="4923.51" x2="85.45" y2="4869.91" />
        </g>
      </g>
    </g>
    <g id="isla34">
      <g id="LINE-331" data-name="LINE">
        <line class="cls-18" x1="1125" y1="4873.87" x2="1002.18" y2="4802.96" />
      </g>
      <g id="LINE-332" data-name="LINE">
        <line class="cls-18" x1="1002.18" y1="4802.96" x2="1125" y2="4732.05" />
      </g>
      <g id="LINE-333" data-name="LINE">
        <polygon class="cls-8"
          points="1125 4590.29 1125 4750.34 1093.85 4732.36 1093.85 4768.87 1002.18 4715.94 1059.87 4682.64 1059.87 4627.9 1125 4590.29" />
      </g>
    </g>
    <g id="isla36">
      <g class="cls-51">
        <image loading="lazy" data-clickable="true" data-category-name="el_cuartel_militar" width="109" height="128"
          transform="translate(828.83 5001.95) scale(2.23)" :href="image36" />
      </g>
      <g class="cls-52">
        <image loading="lazy" data-clickable="true" data-category-name="la_guarderia" width="94" height="124"
          transform="translate(554.78 4944.02) scale(2.23)" :href="image37" />
      </g>
      <g id="LINE-334" data-name="LINE">
        <polygon class="cls-8"
          points="1125 5070.41 1125 5098.8 1059.18 5136.8 1059.18 5089.86 937.37 5019.52 887.64 5028.89 837.92 5076.94 837.92 5123.49 959.74 5193.82 874.21 5243.2 758.75 5176.55 758.75 5154.42 709.61 5098.44 660.46 5097.67 746.52 5047.98 746.52 5024.68 703.58 4972.32 660.64 4975.1 574.58 5024.78 574.58 5053.2 485.84 5001.96 560.09 4959.5 582.7 4972.55 622.28 4949.7 622.28 4913.66 693.03 4872.81 693.03 4858.93 727.13 4817.92 761.22 4819.55 873.4 4884.32 873.4 4901.56 945.41 4943.13 977.44 4924.64 1060.51 4972.61 1060.51 5033.18 1125 5070.41" />
      </g>
      <g>
        <g>
          <g id="LINE-335" data-name="LINE">
            <line class="cls-7" x1="660.46" y1="5201.89" x2="660.46" y2="5097.67" />
          </g>
          <g id="LINE-336" data-name="LINE">
            <line class="cls-7" x1="660.46" y1="5074.36" x2="660.46" y2="5097.67" />
          </g>
          <g id="LINE-337" data-name="LINE">
            <line class="cls-7" x1="660.46" y1="5074.36" x2="617.52" y2="5022" />
          </g>
          <g id="LINE-338" data-name="LINE">
            <line class="cls-7" x1="617.52" y1="5022" x2="703.58" y2="4972.31" />
          </g>
          <g id="LINE-339" data-name="LINE">
            <line class="cls-7" x1="617.52" y1="5022" x2="574.58" y2="5024.78" />
          </g>
          <g id="LINE-340" data-name="LINE">
            <line class="cls-7" x1="746.52" y1="5024.68" x2="660.46" y2="5074.36" />
          </g>
          <g id="LINE-341" data-name="LINE">
            <line class="cls-7" x1="574.58" y1="5053.19" x2="574.58" y2="5152.31" />
          </g>
        </g>
        <g id="LWPOLYLINE-44" data-name="LWPOLYLINE">
          <line class="cls-7" x1="660.46" y1="5201.89" x2="574.58" y2="5152.31" />
        </g>
      </g>
      <g>
        <g id="LINE-342" data-name="LINE">
          <line class="cls-7" x1="959.74" y1="5193.82" x2="959.74" y2="5147.27" />
        </g>
        <g id="LINE-343" data-name="LINE">
          <line class="cls-7" x1="1059.18" y1="5136.8" x2="1059.18" y2="5218.5" />
        </g>
        <g id="LINE-344" data-name="LINE">
          <line class="cls-7" x1="1059.18" y1="5089.85" x2="1009.46" y2="5099.22" />
        </g>
        <g id="LINE-345" data-name="LINE">
          <line class="cls-7" x1="1009.46" y1="5099.22" x2="887.64" y2="5028.89" />
        </g>
        <g id="LINE-346" data-name="LINE">
          <line class="cls-7" x1="1009.46" y1="5099.22" x2="959.74" y2="5147.27" />
        </g>
        <g id="LINE-347" data-name="LINE">
          <line class="cls-7" x1="959.74" y1="5147.27" x2="837.92" y2="5076.94" />
        </g>
        <g id="LINE-348" data-name="LINE">
          <line class="cls-7" x1="959.74" y1="5275.91" x2="959.74" y2="5193.82" />
        </g>
        <g id="LWPOLYLINE-45" data-name="LWPOLYLINE">
          <line class="cls-7" x1="959.74" y1="5275.91" x2="1059.18" y2="5218.5" />
        </g>
      </g>
    </g>
    <g id="isla37">
      <g class="cls-53">
        <image loading="lazy" data-clickable="true" data-category-name="la_plaza_de_toros" width="108" height="104"
          transform="translate(130.6 5125.66) scale(2.29)" :href="image38" />
      </g>
      <g id="LINE-349" data-name="LINE">
        <path class="cls-8"
          d="M496.68,5188.36v-30.24l-68.19,39.36V5332q-32.7-19-65.41-38v-85.14c-2.24-34.11-54.12-63.07-115.87-64.69s-110,24.73-107.75,58.84v51.46l-65.55,37.85V5164.66L9.43,5127.43v46.88L0,5168.86V4834l57.4,33.14v34.36l12.77,7.37L104.69,4889l30.78,3.37,30.78,32.17v36.76l62.35,36,35-20.17,89.39,51.61,17.62-10.17,56.95,32.88v35.25l48.19,27.83L502.53,5099,577,5142Z" />
      </g>
      <g id="SPLINE-14" data-name="SPLINE">
        <path class="cls-18" d="M428.66,5332.11l-.17-.1" />
      </g>
      <g>
        <g id="ELLIPSE-6" data-name="ELLIPSE">
          <path class="cls-7"
            d="M304.39,5262.62c18.73-15.81,9.37-38.13-20.91-49.84s-70-8.4-88.76,7.42c-12.21,10.3-12.87,23.92-1.73,35.65" />
        </g>
        <g id="SPLINE-15" data-name="SPLINE">
          <path class="cls-7" d="M139.47,5283.68q-2.41,36.43,54.7,57.75t114.22,5.27q57.11-16,54.7-52.7" />
        </g>
        <g id="LWPOLYLINE-46" data-name="LWPOLYLINE">
          <line class="cls-7" x1="139.47" y1="5283.68" x2="139.47" y2="5254.47" />
        </g>
        <g id="ELLIPSE-7" data-name="ELLIPSE">
          <path class="cls-7"
            d="M363.09,5213.34a35.14,35.14,0,0,1-.59,4.43c-6.72,33.52-62,55.4-123.39,48.86s-105.77-39-99.05-72.53" />
        </g>
      </g>
    </g>
    <g id="isla38">
      <g id="LINE-350" data-name="LINE">
        <polygon class="cls-8"
          points="1125 5154.83 1125 5324.79 1086.28 5302.43 1086.28 5360.52 1028.16 5326.96 1028.16 5278.82 955.24 5236.72 1013.46 5203.1 1046.15 5221.97 1076.87 5204.24 1076.87 5182.62 1125 5154.83" />
      </g>
    </g>
    <g id="isla39">
      <g id="LINE-351" data-name="LINE" class="cls-36">
        <polygon points="1029.48 5507.69 844.33 5614.59 472.18 5399.73 657.33 5292.83 1029.48 5507.69" />
      </g>
      <g class="cls-54">
        <image loading="lazy" data-clickable="true" data-category-name="el_cementerio" width="113" height="90"
          transform="translate(724.44 5426.49) scale(2.23)" :href="image39" />
      </g>
      <g>
        <g id="LINE-352" data-name="LINE">
          <line class="cls-5" x1="689.39" y1="5338.81" x2="656.95" y2="5320.08" />
        </g>
        <g id="LINE-353" data-name="LINE">
          <line class="cls-5" x1="656.95" y1="5320.08" x2="596.2" y2="5355.15" />
        </g>
        <g id="LINE-354" data-name="LINE">
          <line class="cls-5" x1="596.2" y1="5355.15" x2="628.64" y2="5373.89" />
        </g>
        <g id="LINE-355" data-name="LINE">
          <line class="cls-5" x1="628.64" y1="5373.89" x2="689.39" y2="5338.81" />
        </g>
        <g id="LINE-356" data-name="LINE">
          <line class="cls-5" x1="519.39" y1="5399.5" x2="580.13" y2="5364.43" />
        </g>
        <g id="LINE-357" data-name="LINE">
          <line class="cls-5" x1="580.13" y1="5364.43" x2="612.58" y2="5383.16" />
        </g>
        <g id="LINE-358" data-name="LINE">
          <line class="cls-5" x1="612.58" y1="5383.16" x2="551.83" y2="5418.23" />
        </g>
        <g id="LINE-359" data-name="LINE">
          <line class="cls-5" x1="551.83" y1="5418.23" x2="519.39" y2="5399.5" />
        </g>
        <g id="LINE-360" data-name="LINE">
          <line class="cls-5" x1="705.46" y1="5348.09" x2="644.71" y2="5383.16" />
        </g>
        <g id="LINE-361" data-name="LINE">
          <line class="cls-5" x1="644.71" y1="5383.16" x2="677.15" y2="5401.89" />
        </g>
        <g id="LINE-362" data-name="LINE">
          <line class="cls-5" x1="677.15" y1="5401.89" x2="737.9" y2="5366.82" />
        </g>
        <g id="LINE-363" data-name="LINE">
          <line class="cls-5" x1="737.9" y1="5366.82" x2="705.46" y2="5348.09" />
        </g>
        <g id="LINE-364" data-name="LINE">
          <line class="cls-5" x1="567.9" y1="5427.51" x2="628.64" y2="5392.43" />
        </g>
        <g id="LINE-365" data-name="LINE">
          <line class="cls-5" x1="628.64" y1="5392.43" x2="661.09" y2="5411.17" />
        </g>
        <g id="LINE-366" data-name="LINE">
          <line class="cls-5" x1="661.09" y1="5411.17" x2="600.34" y2="5446.24" />
        </g>
        <g id="LINE-367" data-name="LINE">
          <line class="cls-5" x1="600.34" y1="5446.24" x2="567.9" y2="5427.51" />
        </g>
        <g id="LINE-368" data-name="LINE">
          <line class="cls-5" x1="753.97" y1="5376.09" x2="693.22" y2="5411.17" />
        </g>
        <g id="LINE-369" data-name="LINE">
          <line class="cls-5" x1="693.22" y1="5411.17" x2="725.66" y2="5429.9" />
        </g>
        <g id="LINE-370" data-name="LINE">
          <line class="cls-5" x1="725.66" y1="5429.9" x2="786.41" y2="5394.83" />
        </g>
        <g id="LINE-371" data-name="LINE">
          <line class="cls-5" x1="786.41" y1="5394.83" x2="753.97" y2="5376.09" />
        </g>
        <g id="LINE-372" data-name="LINE">
          <line class="cls-5" x1="616.41" y1="5455.51" x2="677.15" y2="5420.44" />
        </g>
        <g id="LINE-373" data-name="LINE">
          <line class="cls-5" x1="677.15" y1="5420.44" x2="709.6" y2="5439.17" />
        </g>
        <g id="LINE-374" data-name="LINE">
          <line class="cls-5" x1="709.6" y1="5439.17" x2="648.85" y2="5474.25" />
        </g>
        <g id="LINE-375" data-name="LINE">
          <line class="cls-5" x1="648.85" y1="5474.25" x2="616.41" y2="5455.51" />
        </g>
        <g id="LINE-376" data-name="LINE">
          <line class="cls-5" x1="802.48" y1="5404.1" x2="741.73" y2="5439.17" />
        </g>
        <g id="LINE-377" data-name="LINE">
          <line class="cls-5" x1="741.73" y1="5439.17" x2="774.17" y2="5457.91" />
        </g>
        <g id="LINE-378" data-name="LINE">
          <line class="cls-5" x1="774.17" y1="5457.91" x2="834.92" y2="5422.83" />
        </g>
        <g id="LINE-379" data-name="LINE">
          <line class="cls-5" x1="834.92" y1="5422.83" x2="802.48" y2="5404.1" />
        </g>
        <g id="LINE-380" data-name="LINE">
          <line class="cls-5" x1="664.92" y1="5483.52" x2="725.66" y2="5448.45" />
        </g>
        <g id="LINE-381" data-name="LINE">
          <line class="cls-5" x1="725.66" y1="5448.45" x2="758.11" y2="5467.18" />
        </g>
        <g id="LINE-382" data-name="LINE">
          <line class="cls-5" x1="758.11" y1="5467.18" x2="697.36" y2="5502.25" />
        </g>
        <g id="LINE-383" data-name="LINE">
          <line class="cls-5" x1="697.36" y1="5502.25" x2="664.92" y2="5483.52" />
        </g>
        <g id="LINE-384" data-name="LINE">
          <line class="cls-5" x1="835.81" y1="5478.34" x2="883.43" y2="5450.84" />
        </g>
        <g id="LINE-385" data-name="LINE">
          <line class="cls-5" x1="883.43" y1="5450.84" x2="850.99" y2="5432.11" />
        </g>
        <g id="LINE-386" data-name="LINE">
          <line class="cls-5" x1="850.99" y1="5432.11" x2="790.24" y2="5467.18" />
        </g>
        <g id="LINE-387" data-name="LINE">
          <line class="cls-5" x1="790.24" y1="5467.18" x2="793.45" y2="5469.04" />
        </g>
        <g id="LINE-388" data-name="LINE">
          <line class="cls-5" x1="763.55" y1="5520.06" x2="745.87" y2="5530.26" />
        </g>
        <g id="LINE-389" data-name="LINE">
          <line class="cls-5" x1="745.87" y1="5530.26" x2="713.43" y2="5511.53" />
        </g>
        <g id="LINE-390" data-name="LINE">
          <line class="cls-5" x1="713.43" y1="5511.53" x2="774.17" y2="5476.46" />
        </g>
        <g id="LINE-391" data-name="LINE">
          <line class="cls-5" x1="774.17" y1="5476.46" x2="782.38" y2="5481.2" />
        </g>
      </g>
      <g>
        <g id="LINE-392" data-name="LINE">
          <line class="cls-7" x1="937.25" y1="5506.59" x2="888.94" y2="5478.69" />
        </g>
        <g id="LINE-393" data-name="LINE">
          <line class="cls-7" x1="888.94" y1="5478.69" x2="862.68" y2="5493.85" />
        </g>
        <g id="LINE-394" data-name="LINE">
          <line class="cls-7" x1="793.19" y1="5469.07" x2="874.28" y2="5515.89" />
        </g>
        <g id="LINE-395" data-name="LINE">
          <line class="cls-7" x1="844.72" y1="5587.33" x2="844.72" y2="5549.42" />
        </g>
        <g id="LINE-396" data-name="LINE">
          <line class="cls-7" x1="844.72" y1="5549.42" x2="874.28" y2="5515.89" />
        </g>
        <g id="LINE-397" data-name="LINE">
          <line class="cls-7" x1="874.28" y1="5515.89" x2="901.82" y2="5516.45" />
        </g>
        <g id="LINE-398" data-name="LINE">
          <line class="cls-7" x1="901.82" y1="5516.45" x2="820.65" y2="5469.59" />
        </g>
        <g id="LINE-399" data-name="LINE">
          <line class="cls-7" x1="820.65" y1="5469.59" x2="793.11" y2="5469.03" />
        </g>
        <g id="LINE-400" data-name="LINE">
          <line class="cls-7" x1="793.11" y1="5469.03" x2="763.55" y2="5502.55" />
        </g>
        <g id="LINE-401" data-name="LINE">
          <line class="cls-7" x1="763.55" y1="5502.55" x2="844.72" y2="5549.42" />
        </g>
        <g id="LINE-402" data-name="LINE">
          <line class="cls-7" x1="901.82" y1="5516.45" x2="901.82" y2="5527.05" />
        </g>
        <g id="LINE-403" data-name="LINE">
          <line class="cls-7" x1="901.82" y1="5527.05" x2="937.25" y2="5506.59" />
        </g>
        <g id="LINE-404" data-name="LINE">
          <line class="cls-7" x1="937.25" y1="5506.59" x2="937.25" y2="5533.91" />
        </g>
        <g id="LINE-405" data-name="LINE">
          <line class="cls-7" x1="937.25" y1="5533.91" x2="844.72" y2="5587.33" />
        </g>
        <g id="LINE-406" data-name="LINE">
          <line class="cls-7" x1="844.72" y1="5587.33" x2="763.55" y2="5540.47" />
        </g>
        <g id="LINE-407" data-name="LINE">
          <line class="cls-7" x1="763.55" y1="5540.47" x2="763.55" y2="5502.55" />
        </g>
      </g>
    </g>
    <g id="isla40">
      <g id="LINE-408" data-name="LINE" class="cls-36">
        <polygon
          points="799.42 5640.52 219.21 5975.5 0 5848.94 0 5741.18 198.55 5626.54 348.85 5539.77 486.89 5460.07 799.42 5640.52" />
      </g>
      <g>
        <g id="LINE-409" data-name="LINE">
          <line class="cls-7" x1="521.9" y1="5615" x2="467.28" y2="5583.46" />
        </g>
        <g id="LINE-410" data-name="LINE">
          <line class="cls-7" x1="542.3" y1="5613.64" x2="521.9" y2="5615" />
        </g>
        <g id="LINE-411" data-name="LINE">
          <line class="cls-7" x1="521.9" y1="5615" x2="501.5" y2="5637.19" />
        </g>
        <g id="LINE-412" data-name="LINE">
          <line class="cls-7" x1="501.5" y1="5652.8" x2="501.5" y2="5637.19" />
        </g>
        <g id="LINE-413" data-name="LINE">
          <line class="cls-7" x1="501.5" y1="5637.19" x2="446.88" y2="5605.66" />
        </g>
        <g id="LINE-414" data-name="LINE">
          <line class="cls-7" x1="446.88" y1="5605.66" x2="467.28" y2="5583.46" />
        </g>
        <g id="LINE-415" data-name="LINE">
          <line class="cls-7" x1="467.28" y1="5583.46" x2="487.68" y2="5582.1" />
        </g>
        <g id="LINE-416" data-name="LINE">
          <line class="cls-7" x1="487.68" y1="5582.1" x2="542.3" y2="5613.64" />
        </g>
        <g id="LINE-417" data-name="LINE">
          <line class="cls-7" x1="542.3" y1="5613.64" x2="542.3" y2="5629.24" />
        </g>
        <g id="LINE-418" data-name="LINE">
          <line class="cls-7" x1="542.3" y1="5629.24" x2="501.5" y2="5652.8" />
        </g>
        <g id="LINE-419" data-name="LINE">
          <line class="cls-7" x1="501.5" y1="5652.8" x2="446.88" y2="5621.26" />
        </g>
        <g id="LINE-420" data-name="LINE">
          <line class="cls-7" x1="446.88" y1="5621.26" x2="446.88" y2="5605.66" />
        </g>
      </g>
      <g id="LINE-421" data-name="LINE" class="cls-36">
        <polygon points="304.02 5513.88 177.6 5586.87 63.06 5653 0 5616.59 0 5506.75 145.83 5422.56 304.02 5513.88" />
      </g>
      <g class="cls-55">
        <image loading="lazy" data-clickable="true" data-category-name="la_granja" width="170" height="133"
          transform="translate(96.02 5732.11) scale(2.23)" :href="image40" />
      </g>
      <g>
        <g id="LINE-422" data-name="LINE">
          <line class="cls-5" x1="198.55" y1="5626.54" x2="356.74" y2="5717.87" />
        </g>
        <g id="LINE-423" data-name="LINE">
          <line class="cls-5" x1="462.96" y1="5656.55" x2="304.77" y2="5565.22" />
        </g>
        <g id="LINE-424" data-name="LINE">
          <line class="cls-5" x1="383.86" y1="5610.88" x2="565.98" y2="5505.74" />
        </g>
        <g id="LINE-425" data-name="LINE">
          <line class="cls-5" x1="64.86" y1="5886.39" x2="462.96" y2="5656.55" />
        </g>
        <g id="LINE-426" data-name="LINE">
          <line class="cls-5" x1="462.96" y1="5656.55" x2="617.31" y2="5745.66" />
        </g>
        <g id="LINE-427" data-name="LINE">
          <line class="cls-5" x1="689.38" y1="5576.98" x2="507.27" y2="5682.13" />
        </g>
        <g id="LINE-428" data-name="LINE">
          <line class="cls-5" x1="92.33" y1="5687.87" x2="250.52" y2="5779.2" />
        </g>
        <g id="LINE-429" data-name="LINE">
          <line class="cls-5" x1="9.58" y1="5735.65" x2="167.76" y2="5826.98" />
        </g>
        <g id="ARC-95" data-name="ARC">
          <path class="cls-5" d="M529.75,5779.59A276.24,276.24,0,0,0,475.08,5748" />
        </g>
        <g id="ARC-96" data-name="ARC">
          <path class="cls-5" d="M547.24,5769.49a276.77,276.77,0,0,0-54.68-31.56" />
        </g>
        <g id="ARC-97" data-name="ARC">
          <path class="cls-5" d="M564.72,5759.4a277,277,0,0,0-54.67-31.56" />
        </g>
        <g id="ARC-98" data-name="ARC">
          <path class="cls-5" d="M582.2,5749.31a276.24,276.24,0,0,0-54.67-31.57" />
        </g>
        <g id="ARC-99" data-name="ARC">
          <path class="cls-5" d="M512.24,5708.92a194,194,0,0,0-52.45,30.27" />
        </g>
        <g id="ARC-100" data-name="ARC">
          <path class="cls-5" d="M494.76,5698.82a193.79,193.79,0,0,0-52.45,30.28" />
        </g>
        <g id="ARC-101" data-name="ARC">
          <path class="cls-5" d="M477.27,5688.73A193.73,193.73,0,0,0,424.83,5719" />
        </g>
        <g id="ARC-102" data-name="ARC">
          <path class="cls-5" d="M458.77,5678.05a193.58,193.58,0,0,0-52.44,30.28" />
        </g>
        <g id="ARC-103" data-name="ARC">
          <path class="cls-5" d="M515,5789.24a193.79,193.79,0,0,0-52.45,30.28" />
        </g>
        <g id="ARC-104" data-name="ARC">
          <path class="cls-5" d="M497.53,5779.14a193.9,193.9,0,0,0-52.45,30.28" />
        </g>
        <g id="ARC-105" data-name="ARC">
          <path class="cls-5" d="M480,5769.05a193.73,193.73,0,0,0-52.44,30.28" />
        </g>
        <g id="ARC-106" data-name="ARC">
          <path class="cls-5" d="M461.54,5758.37a193.79,193.79,0,0,0-52.45,30.28" />
        </g>
        <g id="LINE-430" data-name="LINE">
          <line class="cls-5" x1="274.19" y1="5783.43" x2="325.8" y2="5753.63" />
        </g>
        <g id="LINE-431" data-name="LINE">
          <line class="cls-5" x1="325.8" y1="5753.63" x2="352.68" y2="5769.15" />
        </g>
        <g id="LINE-432" data-name="LINE">
          <line class="cls-5" x1="352.68" y1="5769.15" x2="301.07" y2="5798.95" />
        </g>
        <g id="LINE-433" data-name="LINE">
          <line class="cls-5" x1="301.07" y1="5798.95" x2="274.19" y2="5783.43" />
        </g>
        <g id="LINE-434" data-name="LINE">
          <line class="cls-5" x1="249.02" y1="5764.1" x2="228.94" y2="5752.51" />
        </g>
        <g id="LINE-435" data-name="LINE">
          <line class="cls-5" x1="228.94" y1="5752.51" x2="249.02" y2="5740.92" />
        </g>
        <g id="LINE-436" data-name="LINE">
          <line class="cls-5" x1="249.02" y1="5740.92" x2="269.1" y2="5752.51" />
        </g>
        <g id="LINE-437" data-name="LINE">
          <line class="cls-5" x1="269.1" y1="5752.51" x2="249.02" y2="5764.1" />
        </g>
        <g id="LINE-438" data-name="LINE">
          <line class="cls-5" x1="204.3" y1="5789.93" x2="184.22" y2="5778.33" />
        </g>
        <g id="LINE-439" data-name="LINE">
          <line class="cls-5" x1="184.22" y1="5778.33" x2="204.3" y2="5766.74" />
        </g>
        <g id="LINE-440" data-name="LINE">
          <line class="cls-5" x1="204.3" y1="5766.74" x2="224.38" y2="5778.33" />
        </g>
        <g id="LINE-441" data-name="LINE">
          <line class="cls-5" x1="224.38" y1="5778.33" x2="204.3" y2="5789.93" />
        </g>
        <g id="LINE-442" data-name="LINE">
          <line class="cls-5" x1="355.24" y1="5702.78" x2="335.16" y2="5691.18" />
        </g>
        <g id="LINE-443" data-name="LINE">
          <line class="cls-5" x1="335.16" y1="5691.18" x2="355.24" y2="5679.59" />
        </g>
        <g id="LINE-444" data-name="LINE">
          <line class="cls-5" x1="355.24" y1="5679.59" x2="375.32" y2="5691.18" />
        </g>
        <g id="LINE-445" data-name="LINE">
          <line class="cls-5" x1="375.32" y1="5691.18" x2="355.24" y2="5702.78" />
        </g>
        <g id="LINE-446" data-name="LINE">
          <line class="cls-5" x1="63.36" y1="5871.29" x2="43.28" y2="5859.7" />
        </g>
        <g id="LINE-447" data-name="LINE">
          <line class="cls-5" x1="43.28" y1="5859.7" x2="63.36" y2="5848.11" />
        </g>
        <g id="LINE-448" data-name="LINE">
          <line class="cls-5" x1="63.36" y1="5848.11" x2="83.44" y2="5859.7" />
        </g>
        <g id="LINE-449" data-name="LINE">
          <line class="cls-5" x1="83.44" y1="5859.7" x2="63.36" y2="5871.29" />
        </g>
        <g id="LINE-450" data-name="LINE">
          <line class="cls-5" x1="622.46" y1="5594.67" x2="589.6" y2="5575.7" />
        </g>
        <g id="LINE-451" data-name="LINE">
          <line class="cls-5" x1="589.6" y1="5575.7" x2="622.46" y2="5556.72" />
        </g>
        <g id="LINE-452" data-name="LINE">
          <line class="cls-5" x1="622.46" y1="5556.72" x2="655.33" y2="5575.7" />
        </g>
        <g id="LINE-453" data-name="LINE">
          <line class="cls-5" x1="655.33" y1="5575.7" x2="622.46" y2="5594.67" />
        </g>
        <g id="ARC-107" data-name="ARC">
          <path class="cls-5" d="M763,5638.18a401.83,401.83,0,0,0-73.82-42.62" />
        </g>
        <g id="ARC-108" data-name="ARC">
          <path class="cls-5" d="M664,5674.42A329.82,329.82,0,0,0,595.44,5714" />
        </g>
        <g id="ARC-109" data-name="ARC">
          <path class="cls-5" d="M646.47,5664.33A330.23,330.23,0,0,0,578,5703.88" />
        </g>
        <g id="ARC-110" data-name="ARC">
          <path class="cls-5" d="M629,5654.24a329.08,329.08,0,0,0-68.51,39.55" />
        </g>
        <g id="ARC-111" data-name="ARC">
          <path class="cls-5" d="M610.48,5643.55A329.82,329.82,0,0,0,542,5683.11" />
        </g>
        <g id="ARC-112" data-name="ARC">
          <path class="cls-5" d="M681.43,5684.51a329.82,329.82,0,0,0-68.51,39.56" />
        </g>
        <g id="ARC-113" data-name="ARC">
          <path class="cls-5" d="M745.56,5648.28a401.59,401.59,0,0,0-73.82-42.62" />
        </g>
        <g id="ARC-114" data-name="ARC">
          <path class="cls-5" d="M728.08,5658.37a402.16,402.16,0,0,0-73.82-42.62" />
        </g>
        <g id="ARC-115" data-name="ARC">
          <path class="cls-5" d="M710.6,5668.46a402.16,402.16,0,0,0-73.82-42.62" />
        </g>
        <g id="ARC-116" data-name="ARC">
          <path class="cls-5" d="M693.11,5678.56a401.51,401.51,0,0,0-73.81-42.62" />
        </g>
        <g id="ARC-117" data-name="ARC">
          <path class="cls-5" d="M484.61,5536.09a276.69,276.69,0,0,0-54.67-31.56" />
        </g>
        <g id="ARC-118" data-name="ARC">
          <path class="cls-5" d="M502.09,5526a276.69,276.69,0,0,0-54.67-31.56" />
        </g>
        <g id="ARC-119" data-name="ARC">
          <path class="cls-5" d="M519.57,5515.91a276.24,276.24,0,0,0-54.67-31.57" />
        </g>
        <g id="ARC-120" data-name="ARC">
          <path class="cls-5" d="M537.05,5505.81a276.69,276.69,0,0,0-54.67-31.56" />
        </g>
        <g id="ARC-121" data-name="ARC">
          <path class="cls-5" d="M469.86,5545.74A193.58,193.58,0,0,0,417.42,5576" />
        </g>
        <g id="ARC-122" data-name="ARC">
          <path class="cls-5" d="M452.38,5535.65a193.79,193.79,0,0,0-52.45,30.28" />
        </g>
        <g id="ARC-123" data-name="ARC">
          <path class="cls-5" d="M434.9,5525.56a193.79,193.79,0,0,0-52.45,30.28" />
        </g>
        <g id="ARC-124" data-name="ARC">
          <path class="cls-5" d="M416.39,5514.87A194,194,0,0,0,364,5545.15" />
        </g>
        <g id="LINE-454" data-name="LINE">
          <line class="cls-5" x1="398.77" y1="5585.86" x2="347.16" y2="5556.06" />
        </g>
        <g id="LINE-455" data-name="LINE">
          <line class="cls-5" x1="347.16" y1="5556.06" x2="331.03" y2="5565.37" />
        </g>
        <g id="LINE-456" data-name="LINE">
          <line class="cls-5" x1="331.03" y1="5565.37" x2="382.65" y2="5595.17" />
        </g>
        <g id="LINE-457" data-name="LINE">
          <line class="cls-5" x1="382.65" y1="5595.17" x2="398.77" y2="5585.86" />
        </g>
      </g>
      <g>
        <g id="LINE-458" data-name="LINE">
          <line class="cls-7" x1="143.82" y1="5904.67" x2="143.82" y2="5931.98" />
        </g>
        <g>
          <g id="LINE-459" data-name="LINE">
            <line class="cls-7" x1="420.16" y1="5859.49" x2="420.16" y2="5832.18" />
          </g>
          <g>
            <g id="LINE-460" data-name="LINE">
              <line class="cls-7" x1="219.21" y1="5948.2" x2="219.21" y2="5975.5" />
            </g>
            <g id="LINE-461" data-name="LINE">
              <line class="cls-7" x1="181.52" y1="5912.67" x2="143.82" y2="5904.67" />
            </g>
            <g id="LINE-462" data-name="LINE">
              <line class="cls-7" x1="143.82" y1="5904.67" x2="344.77" y2="5788.65" />
            </g>
            <g id="LINE-463" data-name="LINE">
              <line class="cls-7" x1="344.77" y1="5788.65" x2="382.46" y2="5796.66" />
            </g>
            <g id="LINE-464" data-name="LINE">
              <line class="cls-7" x1="219.21" y1="5948.2" x2="181.52" y2="5912.67" />
            </g>
            <g id="LINE-465" data-name="LINE">
              <line class="cls-7" x1="181.52" y1="5912.67" x2="382.46" y2="5796.66" />
            </g>
            <g id="LINE-466" data-name="LINE">
              <line class="cls-7" x1="382.46" y1="5796.66" x2="420.16" y2="5832.18" />
            </g>
            <g id="LINE-467" data-name="LINE">
              <line class="cls-7" x1="420.16" y1="5832.18" x2="219.21" y2="5948.2" />
            </g>
            <g id="LINE-468" data-name="LINE">
              <line class="cls-7" x1="420.16" y1="5859.49" x2="219.21" y2="5975.5" />
            </g>
            <g id="LINE-469" data-name="LINE">
              <line class="cls-7" x1="219.21" y1="5975.5" x2="143.82" y2="5931.98" />
            </g>
          </g>
        </g>
      </g>
      <g>
        <g id="ELLIPSE-8" data-name="ELLIPSE">
          <path class="cls-7"
            d="M417.35,5740c.57-8.6-11.66-16.41-27.32-17.44s-28.82,5.09-29.39,13.69,11.67,16.41,27.33,17.45,28.81-5.1,29.38-13.7Z" />
        </g>
        <g id="SPLINE-16" data-name="SPLINE">
          <path class="cls-7" d="M360.75,5735.29l-.07,14.15" />
        </g>
        <g id="SPLINE-17" data-name="SPLINE">
          <path class="cls-7" d="M360.68,5749.44q-1,15.15,26.56,17.39t30.05-12.8" />
        </g>
        <g id="SPLINE-18" data-name="SPLINE">
          <path class="cls-7" d="M417.29,5754l.08-14.44" />
        </g>
      </g>
      <g>
        <g id="LINE-470" data-name="LINE">
          <line class="cls-7" x1="206.13" y1="5517.09" x2="206.13" y2="5551.28" />
        </g>
        <g id="LINE-471" data-name="LINE">
          <line class="cls-7" x1="172.03" y1="5497.4" x2="172.03" y2="5531.59" />
        </g>
        <g id="LINE-472" data-name="LINE">
          <line class="cls-7" x1="244.72" y1="5529.01" x2="206.13" y2="5551.28" />
        </g>
        <g id="LINE-473" data-name="LINE">
          <line class="cls-7" x1="206.13" y1="5551.28" x2="172.03" y2="5531.59" />
        </g>
        <g id="LINE-474" data-name="LINE">
          <line class="cls-7" x1="244.72" y1="5509.65" x2="244.72" y2="5529.01" />
        </g>
        <g id="LINE-475" data-name="LINE">
          <line class="cls-7" x1="172.03" y1="5497.4" x2="206.13" y2="5517.09" />
        </g>
        <g id="LINE-476" data-name="LINE">
          <line class="cls-7" x1="206.13" y1="5517.09" x2="244.72" y2="5509.65" />
        </g>
        <g id="LINE-477" data-name="LINE">
          <line class="cls-7" x1="244.72" y1="5509.65" x2="210.61" y2="5489.96" />
        </g>
        <g id="LINE-478" data-name="LINE">
          <line class="cls-7" x1="210.61" y1="5489.96" x2="172.03" y2="5497.4" />
        </g>
      </g>
      <g>
        <g id="LINE-479" data-name="LINE">
          <line class="cls-7" x1="176.14" y1="5585.4" x2="198.55" y2="5607.97" />
        </g>
        <g id="LINE-480" data-name="LINE">
          <line class="cls-7" x1="150.36" y1="5635.79" x2="198.55" y2="5607.97" />
        </g>
        <g id="LINE-481" data-name="LINE">
          <line class="cls-7" x1="198.55" y1="5607.97" x2="198.55" y2="5626.54" />
        </g>
        <g id="LINE-482" data-name="LINE">
          <line class="cls-7" x1="127.94" y1="5613.22" x2="105.53" y2="5609.91" />
        </g>
        <g id="LINE-483" data-name="LINE">
          <line class="cls-7" x1="105.53" y1="5609.91" x2="153.72" y2="5582.08" />
        </g>
        <g id="LINE-484" data-name="LINE">
          <line class="cls-7" x1="105.53" y1="5628.48" x2="150.36" y2="5654.37" />
        </g>
        <g id="LINE-485" data-name="LINE">
          <line class="cls-7" x1="150.36" y1="5654.37" x2="150.36" y2="5635.79" />
        </g>
        <g id="LINE-486" data-name="LINE">
          <line class="cls-7" x1="150.36" y1="5635.79" x2="127.94" y2="5613.22" />
        </g>
        <g id="LINE-487" data-name="LINE">
          <line class="cls-7" x1="127.94" y1="5613.22" x2="176.14" y2="5585.4" />
        </g>
        <g id="LINE-488" data-name="LINE">
          <line class="cls-7" x1="176.14" y1="5585.4" x2="153.72" y2="5582.1" />
        </g>
        <g id="LINE-489" data-name="LINE">
          <line class="cls-7" x1="150.36" y1="5654.37" x2="198.55" y2="5626.54" />
        </g>
        <g id="LINE-490" data-name="LINE">
          <line class="cls-7" x1="105.53" y1="5609.91" x2="105.53" y2="5628.48" />
        </g>
      </g>
      <g>
        <g id="LINE-491" data-name="LINE">
          <line class="cls-7" y1="5488.18" x2="47.61" y2="5460.69" />
        </g>
        <g id="LINE-492" data-name="LINE">
          <line class="cls-7" x1="47.61" y1="5460.69" x2="47.61" y2="5479.26" />
        </g>
        <g id="LINE-493" data-name="LINE">
          <line class="cls-7" x1="47.61" y1="5479.26" y2="5506.75" />
        </g>
        <g id="LINE-494" data-name="LINE">
          <line class="cls-7" y1="5506.75" y2="5437.84" />
        </g>
        <g id="LINE-495" data-name="LINE">
          <line class="cls-7" y1="5437.84" x2="11.61" y2="5431.13" />
        </g>
        <g id="LINE-496" data-name="LINE">
          <line class="cls-7" x1="11.61" y1="5431.13" x2="47.61" y2="5460.69" />
        </g>
      </g>
      <g id="LINE-497" data-name="LINE">
        <line class="cls-5" x1="47.61" y1="5479.26" x2="205.8" y2="5570.59" />
      </g>
      <line class="cls-56" x1="304.77" y1="5565.22" y2="5741.18" />
      <line class="cls-56" x1="64.86" y1="5886.39" y2="5848.94" />
      <line class="cls-57" x1="47.61" y1="5479.26" x2="145.83" y2="5422.56" />
      <line class="cls-57" x1="145.83" y1="5422.56" x2="304.02" y2="5513.88" />
      <line class="cls-57" x1="63.06" y1="5653" y2="5616.59" />
      <line class="cls-57" x1="63.06" y1="5653" x2="105.53" y2="5628.48" />
      <line class="cls-57" x1="304.02" y1="5513.88" x2="177.6" y2="5586.87" />
      <g id="ELLIPSE-9" data-name="ELLIPSE">
        <path class="cls-7"
          d="M596.92,5539.07c.5-7.6-10.31-14.5-24.15-15.42s-25.46,4.5-26,12.1,10.3,14.5,24.14,15.42,25.46-4.5,26-12.1Z" />
      </g>
      <g id="SPLINE-19" data-name="SPLINE">
        <path class="cls-7" d="M546.91,5534.93l-.07,12.5" />
      </g>
      <g id="SPLINE-20" data-name="SPLINE">
        <path class="cls-7" d="M546.84,5547.43q-.89,13.39,23.47,15.37t26.56-11.31" />
      </g>
      <g id="SPLINE-21" data-name="SPLINE">
        <path class="cls-7" d="M596.87,5551.49l.06-12.76" />
      </g>
    </g>
    <g id="isla41">
      <g class="cls-36">
        <g id="LINE-498" data-name="LINE">
          <polygon
            points="1125.01 5562.83 1125.01 5908.46 908.23 6033.62 594.4 5852.43 1110.51 5554.46 1125.01 5562.83" />
        </g>
      </g>
      <g class="cls-58">
        <image loading="lazy" data-clickable="true" data-category-name="el_zoo" width="136" height="100"
          transform="translate(717.83 5669.03) scale(2.23)" :href="image41" />
      </g>
      <g>
        <g id="LINE-499" data-name="LINE">
          <line class="cls-5" x1="981.35" y1="5953.49" x2="873.1" y2="5890.99" />
        </g>
        <g id="LINE-500" data-name="LINE">
          <line class="cls-5" x1="873.1" y1="5890.99" x2="797.8" y2="5934.47" />
        </g>
        <g id="LINE-501" data-name="LINE">
          <line class="cls-5" x1="797.8" y1="5934.47" x2="906.05" y2="5996.97" />
        </g>
        <g id="LINE-502" data-name="LINE">
          <line class="cls-5" x1="906.05" y1="5996.97" x2="981.35" y2="5953.49" />
        </g>
        <g id="LINE-503" data-name="LINE">
          <line class="cls-5" x1="1087.92" y1="5891.96" x2="1011.23" y2="5936.24" />
        </g>
        <g id="LINE-504" data-name="LINE">
          <line class="cls-5" x1="1011.23" y1="5936.24" x2="929.5" y2="5889.05" />
        </g>
        <g id="LINE-505" data-name="LINE">
          <line class="cls-5" x1="929.5" y1="5889.05" x2="1006.19" y2="5844.78" />
        </g>
        <g id="LINE-506" data-name="LINE">
          <line class="cls-5" x1="1006.19" y1="5844.78" x2="1087.92" y2="5891.96" />
        </g>
        <g id="LINE-507" data-name="LINE">
          <line class="cls-5" x1="970.37" y1="5912.65" x2="1047.05" y2="5868.37" />
        </g>
        <g id="LINE-508" data-name="LINE">
          <line class="cls-5" x1="843.75" y1="5874.05" x2="735.5" y2="5811.55" />
        </g>
        <g id="LINE-509" data-name="LINE">
          <line class="cls-5" x1="735.5" y1="5811.55" x2="660.2" y2="5855.03" />
        </g>
        <g id="LINE-510" data-name="LINE">
          <line class="cls-5" x1="660.2" y1="5855.03" x2="768.45" y2="5917.52" />
        </g>
        <g id="LINE-511" data-name="LINE">
          <line class="cls-5" x1="768.45" y1="5917.52" x2="843.75" y2="5874.05" />
        </g>
        <g id="LINE-512" data-name="LINE">
          <line class="cls-5" x1="1036.32" y1="5645.19" x2="1104.11" y2="5684.33" />
        </g>
        <g id="LINE-513" data-name="LINE">
          <line class="cls-5" x1="1104.11" y1="5684.33" x2="1000.5" y2="5744.15" />
        </g>
        <g id="LINE-514" data-name="LINE">
          <line class="cls-5" x1="1000.5" y1="5744.15" x2="932.71" y2="5705.01" />
        </g>
        <g id="LINE-515" data-name="LINE">
          <line class="cls-5" x1="932.71" y1="5705.01" x2="1036.32" y2="5645.19" />
        </g>
        <g id="LINE-516" data-name="LINE">
          <line class="cls-5" x1="1052.31" y1="5714.24" x2="984.52" y2="5675.1" />
        </g>
        <g id="LINE-517" data-name="LINE">
          <line class="cls-5" x1="1093.13" y1="5643.49" x2="1125" y2="5625.08" />
        </g>
        <g id="LINE-518" data-name="LINE">
          <line class="cls-5" x1="1115.87" y1="5583.17" x2="1125" y2="5588.44" />
        </g>
        <g id="LINE-519" data-name="LINE">
          <line class="cls-5" x1="1125" y1="5661.89" x2="1052.26" y2="5619.89" />
        </g>
        <g id="LINE-520" data-name="LINE">
          <line class="cls-5" x1="1052.26" y1="5619.89" x2="1115.87" y2="5583.17" />
        </g>
        <g id="LINE-521" data-name="LINE">
          <line class="cls-5" x1="1125" y1="5749.46" x2="1084.13" y2="5725.86" />
        </g>
        <g id="LINE-522" data-name="LINE">
          <line class="cls-5" x1="1084.13" y1="5725.86" x2="1125" y2="5702.26" />
        </g>
      </g>
      <g id="LINE-523" data-name="LINE">
        <line class="cls-18" x1="1125" y1="5845.65" x2="1125" y2="5783.34" />
      </g>
      <g>
        <g id="LINE-524" data-name="LINE">
          <line class="cls-7" x1="974.79" y1="5760.08" x2="922.79" y2="5774.72" />
        </g>
        <g id="LINE-525" data-name="LINE">
          <line class="cls-7" x1="841.62" y1="5727.86" x2="922.79" y2="5774.72" />
        </g>
        <g id="LINE-526" data-name="LINE">
          <line class="cls-7" x1="922.79" y1="5774.72" x2="870.79" y2="5820.13" />
        </g>
        <g id="LINE-527" data-name="LINE">
          <line class="cls-7" x1="789.62" y1="5773.26" x2="870.79" y2="5820.13" />
        </g>
        <g id="LINE-528" data-name="LINE">
          <line class="cls-7" x1="870.79" y1="5820.13" x2="870.79" y2="5844.4" />
        </g>
        <g id="LINE-529" data-name="LINE">
          <line class="cls-7" x1="894.35" y1="5713.64" x2="974.79" y2="5760.08" />
        </g>
        <g id="LINE-530" data-name="LINE">
          <line class="cls-7" x1="974.79" y1="5760.08" x2="974.79" y2="5779.53" />
        </g>
        <g id="LINE-531" data-name="LINE">
          <line class="cls-7" x1="974.79" y1="5779.53" x2="870.79" y2="5844.4" />
        </g>
        <g id="LINE-532" data-name="LINE">
          <line class="cls-7" x1="870.79" y1="5844.4" x2="789.62" y2="5797.53" />
        </g>
        <g id="LINE-533" data-name="LINE">
          <line class="cls-7" x1="789.62" y1="5797.53" x2="789.62" y2="5773.26" />
        </g>
        <g id="LINE-534" data-name="LINE">
          <line class="cls-7" x1="789.62" y1="5773.26" x2="841.62" y2="5727.86" />
        </g>
        <g id="LINE-535" data-name="LINE">
          <line class="cls-7" x1="841.62" y1="5727.86" x2="894.35" y2="5713.64" />
        </g>
      </g>
      <g>
        <g id="LINE-536" data-name="LINE">
          <line class="cls-7" x1="1091.44" y1="5826.42" x2="1020.12" y2="5785.25" />
        </g>
        <g id="LINE-537" data-name="LINE">
          <line class="cls-7" x1="1020.12" y1="5785.25" x2="1020.12" y2="5823.85" />
        </g>
        <g id="LINE-538" data-name="LINE">
          <line class="cls-7" x1="1020.12" y1="5823.85" x2="1091.44" y2="5865.02" />
        </g>
        <g id="LINE-539" data-name="LINE">
          <line class="cls-7" x1="1125" y1="5807.05" x2="1091.44" y2="5826.42" />
        </g>
        <g id="LINE-540" data-name="LINE">
          <line class="cls-7" x1="1091.44" y1="5826.42" x2="1091.44" y2="5865.02" />
        </g>
        <g id="LINE-541" data-name="LINE">
          <line class="cls-7" x1="1091.44" y1="5865.02" x2="1125" y2="5845.65" />
        </g>
        <g id="LINE-542" data-name="LINE">
          <line class="cls-7" x1="1125" y1="5783.34" x2="1074.21" y2="5754.02" />
        </g>
        <g id="LINE-543" data-name="LINE">
          <line class="cls-7" x1="1074.21" y1="5754.02" x2="1020.12" y2="5785.25" />
        </g>
      </g>
    </g>
    <g id="isla42">
      <g id="LINE-544" data-name="LINE" class="cls-36">
        <polygon
          points="863.32 6059.55 568.57 6229.73 254.76 6048.53 480.7 5918.09 549.51 5878.36 610.83 5913.77 863.32 6059.55" />
      </g>
      <g class="cls-59">
        <image loading="lazy" data-clickable="true" data-category-name="la_central_electrica" width="186" height="155"
          transform="translate(360.76 5903.73) scale(2.23)" :href="image42" />
      </g>
      <g>
        <g id="LINE-545" data-name="LINE">
          <line class="cls-5" x1="373.34" y1="6088.44" x2="402.66" y2="6071.51" />
        </g>
        <g id="LINE-546" data-name="LINE">
          <line class="cls-5" x1="402.66" y1="6071.51" x2="339.64" y2="6035.12" />
        </g>
        <g id="LINE-547" data-name="LINE">
          <line class="cls-5" x1="339.64" y1="6035.12" x2="310.31" y2="6052.05" />
        </g>
        <g id="LINE-548" data-name="LINE">
          <line class="cls-5" x1="310.31" y1="6052.05" x2="373.34" y2="6088.44" />
        </g>
        <g id="LINE-549" data-name="LINE">
          <line class="cls-5" x1="433.52" y1="6123.18" x2="473.63" y2="6100.02" />
        </g>
        <g id="LINE-550" data-name="LINE">
          <line class="cls-5" x1="473.63" y1="6100.02" x2="429.17" y2="6074.35" />
        </g>
        <g id="LINE-551" data-name="LINE">
          <line class="cls-5" x1="429.17" y1="6074.35" x2="389.06" y2="6097.51" />
        </g>
        <g id="LINE-552" data-name="LINE">
          <line class="cls-5" x1="389.06" y1="6097.51" x2="433.52" y2="6123.18" />
        </g>
        <g id="LINE-553" data-name="LINE">
          <line class="cls-5" x1="523.02" y1="6061.85" x2="486.93" y2="6041.01" />
        </g>
        <g id="LINE-554" data-name="LINE">
          <line class="cls-5" x1="486.93" y1="6041.01" x2="446.82" y2="6064.17" />
        </g>
        <g id="LINE-555" data-name="LINE">
          <line class="cls-5" x1="446.82" y1="6064.17" x2="491.28" y2="6089.83" />
        </g>
        <g id="LINE-556" data-name="LINE">
          <line class="cls-5" x1="491.28" y1="6089.83" x2="519.87" y2="6073.32" />
        </g>
        <g id="LINE-557" data-name="LINE">
          <line class="cls-5" x1="553.8" y1="5957.47" x2="513.97" y2="5934.47" />
        </g>
        <g id="LINE-558" data-name="LINE">
          <line class="cls-5" x1="513.97" y1="5934.47" x2="484.64" y2="5951.4" />
        </g>
        <g id="LINE-559" data-name="LINE">
          <line class="cls-5" x1="484.64" y1="5951.4" x2="531.71" y2="5978.58" />
        </g>
        <g id="LINE-560" data-name="LINE">
          <line class="cls-5" x1="610.82" y1="5951.32" x2="601.04" y2="5956.97" />
        </g>
        <g id="LINE-561" data-name="LINE">
          <line class="cls-5" x1="610.82" y1="5938.04" x2="559.3" y2="5908.29" />
        </g>
        <g id="LINE-562" data-name="LINE">
          <line class="cls-5" x1="559.3" y1="5908.29" x2="529.98" y2="5925.22" />
        </g>
        <g id="LINE-563" data-name="LINE">
          <line class="cls-5" x1="529.98" y1="5925.22" x2="579.72" y2="5953.94" />
        </g>
      </g>
      <g>
        <g id="LINE-564" data-name="LINE">
          <line class="cls-7" x1="499.11" y1="5978.97" x2="424.42" y2="6022.1" />
        </g>
        <g id="LINE-565" data-name="LINE">
          <line class="cls-7" x1="382.38" y1="5997.83" x2="424.42" y2="6022.1" />
        </g>
        <g id="LINE-566" data-name="LINE">
          <line class="cls-7" x1="424.42" y1="6022.1" x2="424.42" y2="6045.07" />
        </g>
        <g id="LINE-567" data-name="LINE">
          <line class="cls-7" x1="424.42" y1="6045.07" x2="499.11" y2="6001.95" />
        </g>
        <g id="LINE-568" data-name="LINE">
          <line class="cls-7" x1="499.11" y1="6001.95" x2="499.11" y2="5978.97" />
        </g>
        <g id="LINE-569" data-name="LINE">
          <line class="cls-7" x1="499.11" y1="5978.97" x2="457.07" y2="5954.7" />
        </g>
        <g id="LINE-570" data-name="LINE">
          <line class="cls-7" x1="457.07" y1="5954.7" x2="382.38" y2="5997.83" />
        </g>
        <g id="LINE-571" data-name="LINE">
          <line class="cls-7" x1="382.38" y1="5997.83" x2="382.38" y2="6020.8" />
        </g>
        <g id="LINE-572" data-name="LINE">
          <line class="cls-7" x1="382.38" y1="6020.8" x2="424.42" y2="6045.07" />
        </g>
      </g>
      <g>
        <g id="ELLIPSE-10" data-name="ELLIPSE">
          <path class="cls-7"
            d="M644,5821.43c.33-5-6.82-9.59-16-10.19s-16.84,3-17.18,8,6.82,9.59,16,10.19,16.84-3,17.18-8Z" />
        </g>
        <g id="ELLIPSE-11" data-name="ELLIPSE">
          <path class="cls-7" d="M630.06,6018.3a22,22,0,0,0,9.47-2.35" />
        </g>
        <g id="LINE-573" data-name="LINE">
          <line class="cls-7" x1="610.82" y1="5819.24" x2="610.82" y2="5960.37" />
        </g>
        <g id="LINE-574" data-name="LINE">
          <line class="cls-7" x1="643.97" y1="5821.43" x2="643.97" y2="6002.37" />
        </g>
        <g id="LINE-575" data-name="LINE">
          <line class="cls-7" x1="611.01" y1="5820.97" x2="610.82" y2="5820.86" />
        </g>
      </g>
      <g>
        <g id="ELLIPSE-12" data-name="ELLIPSE">
          <path class="cls-7"
            d="M756.53,5913.23c1-15.23-20.66-29.07-48.4-30.9s-51,9-52.06,24.26,20.66,29.06,48.41,30.9,51-9,52-24.26Z" />
        </g>
        <g id="ELLIPSE-13" data-name="ELLIPSE">
          <path class="cls-7"
            d="M632.19,5985c1-15.23-20.67-29.07-48.41-30.9s-51,9-52,24.26,20.66,29.06,48.4,30.9,51-9,52.06-24.26Z" />
        </g>
        <g id="ARC-125" data-name="ARC">
          <path class="cls-7" d="M631,6037.3a291,291,0,0,0,25.07-128.7" />
        </g>
        <g id="SPLINE-22" data-name="SPLINE">
          <path class="cls-7" d="M531.73,5980.39a287.16,287.16,0,0,1-26.81,132.5" />
        </g>
        <g id="SPLINE-23" data-name="SPLINE">
          <path class="cls-7" d="M504.92,6112.89q-10.67,27.2,31.94,45t85.22,3.94q42.61-13.84,32-42" />
        </g>
        <g id="SPLINE-24" data-name="SPLINE">
          <path class="cls-7" d="M654.05,6119.79a230.74,230.74,0,0,1-22.26-132.18" />
        </g>
        <g id="SPLINE-25" data-name="SPLINE">
          <path class="cls-7" d="M636.14,6069.44q30.63,34,93.34,24.53t48.91-46" />
        </g>
        <g id="SPLINE-26" data-name="SPLINE">
          <path class="cls-7" d="M778.39,6048a230.84,230.84,0,0,1-22.25-132.19" />
        </g>
      </g>
    </g>
    <g id="isla43">
      <g id="LWPOLYLINE-47" data-name="LWPOLYLINE" class="cls-36">
        <polygon points="1125 5960.24 1125 6457.49 1044.03 6504.24 613.4 6255.61 1125 5960.24" />
      </g>
      <g class="cls-60">
        <image loading="lazy" data-clickable="true" data-category-name="la_depuradora" width="715" height="702"
          transform="translate(744.61 6090.68) scale(0.43)" :href="image43" />
      </g>
      <g>
        <g id="ELLIPSE-14" data-name="ELLIPSE">
          <path class="cls-5"
            d="M799.71,6257.2c1.12-16.9-22.93-32.26-53.72-34.3s-56.66,10-57.78,26.92,22.93,32.27,53.73,34.31,56.66-10,57.77-26.93Z" />
        </g>
        <g id="ELLIPSE-15" data-name="ELLIPSE">
          <path class="cls-5"
            d="M888.23,6206.1c1.12-16.91-22.93-32.27-53.72-34.31s-56.66,10-57.78,26.93,22.93,32.26,53.72,34.3,56.66-10,57.78-26.92Z" />
        </g>
        <g id="ELLIPSE-16" data-name="ELLIPSE">
          <path class="cls-5"
            d="M1075.15,6098.18c1.12-16.91-22.94-32.26-53.73-34.3s-56.66,10-57.78,26.92,22.94,32.27,53.73,34.3,56.66-10,57.78-26.92Z" />
        </g>
        <g id="LINE-576" data-name="LINE">
          <line class="cls-5" x1="1042.25" y1="6477.46" x2="1090.34" y2="6449.69" />
        </g>
        <g id="LINE-577" data-name="LINE">
          <line class="cls-5" x1="1090.34" y1="6449.69" x2="824.49" y2="6296.21" />
        </g>
        <g id="LINE-578" data-name="LINE">
          <line class="cls-5" x1="824.49" y1="6296.21" x2="776.4" y2="6323.97" />
        </g>
        <g id="LINE-579" data-name="LINE">
          <line class="cls-5" x1="776.4" y1="6323.97" x2="1042.25" y2="6477.46" />
        </g>
        <g id="LINE-580" data-name="LINE">
          <line class="cls-5" x1="856.61" y1="6149.23" x2="909.66" y2="6118.6" />
        </g>
        <g id="LINE-581" data-name="LINE">
          <line class="cls-5" x1="909.66" y1="6118.6" x2="963.42" y2="6149.64" />
        </g>
        <g id="LINE-582" data-name="LINE">
          <line class="cls-5" x1="963.42" y1="6149.64" x2="910.37" y2="6180.27" />
        </g>
        <g id="LINE-583" data-name="LINE">
          <line class="cls-5" x1="910.37" y1="6180.27" x2="856.61" y2="6149.23" />
        </g>
        <g id="LINE-584" data-name="LINE">
          <line class="cls-5" x1="1018.12" y1="6381.26" x2="1125" y2="6319.55" />
        </g>
        <g id="LINE-585" data-name="LINE">
          <line class="cls-5" x1="1125" y1="6319.55" x2="1125" y2="6236.19" />
        </g>
        <g id="LINE-586" data-name="LINE">
          <line class="cls-5" x1="1125" y1="6236.19" x2="945.93" y2="6339.58" />
        </g>
        <g id="LINE-587" data-name="LINE">
          <line class="cls-5" x1="945.93" y1="6339.58" x2="1018.12" y2="6381.26" />
        </g>
        <g id="LINE-588" data-name="LINE">
          <line class="cls-5" x1="1113.49" y1="6436.32" x2="1125" y2="6429.68" />
        </g>
        <g id="LINE-589" data-name="LINE">
          <line class="cls-5" x1="1125" y1="6429.68" x2="1125" y2="6346.32" />
        </g>
        <g id="LINE-590" data-name="LINE">
          <line class="cls-5" x1="1125" y1="6346.32" x2="1041.3" y2="6394.64" />
        </g>
        <g id="LINE-591" data-name="LINE">
          <line class="cls-5" x1="1041.3" y1="6394.64" x2="1113.49" y2="6436.32" />
        </g>
        <g id="SPLINE-27" data-name="SPLINE">
          <path class="cls-5" d="M1125,6014.92q-38.51-8.6-62.25,8.34t0,36.08q23.74,19.13,62.25,14.08" />
        </g>
        <g id="SPLINE-28" data-name="SPLINE">
          <path class="cls-5" d="M1125,6073.42v-58.5" />
        </g>
        <g id="SPLINE-29" data-name="SPLINE">
          <path class="cls-5" d="M1125,6119.16q-36.87-6.1-58,10.14t0,34.43q21.15,18.18,58,15.49" />
        </g>
        <g id="SPLINE-30" data-name="SPLINE">
          <path class="cls-5" d="M1125,6179.22v-60.06" />
        </g>
      </g>
      <g>
        <g id="LINE-592" data-name="LINE">
          <line class="cls-7" x1="922.82" y1="6326.24" x2="922.82" y2="6290.5" />
        </g>
        <g>
          <g id="LINE-593" data-name="LINE">
            <line class="cls-7" x1="1028.03" y1="6244.84" x2="922.82" y2="6290.5" />
          </g>
          <g id="LINE-594" data-name="LINE">
            <line class="cls-7" x1="922.82" y1="6290.5" x2="847.65" y2="6247.1" />
          </g>
          <g id="LINE-595" data-name="LINE">
            <line class="cls-7" x1="847.65" y1="6247.1" x2="847.65" y2="6282.84" />
          </g>
          <g id="LINE-596" data-name="LINE">
            <line class="cls-7" x1="847.65" y1="6282.84" x2="922.82" y2="6326.24" />
          </g>
          <g id="LINE-597" data-name="LINE">
            <line class="cls-7" x1="922.82" y1="6326.24" x2="1028.03" y2="6265.49" />
          </g>
          <g id="LINE-598" data-name="LINE">
            <line class="cls-7" x1="1028.03" y1="6265.49" x2="1028.03" y2="6244.84" />
          </g>
          <g id="LINE-599" data-name="LINE">
            <line class="cls-7" x1="1028.03" y1="6244.84" x2="952.86" y2="6201.43" />
          </g>
          <g id="LINE-600" data-name="LINE">
            <line class="cls-7" x1="952.86" y1="6201.43" x2="847.65" y2="6247.1" />
          </g>
        </g>
      </g>
      <g>
        <g id="ELLIPSE-17" data-name="ELLIPSE">
          <path class="cls-7"
            d="M1094.79,6205.89c.57-8.6-11.66-16.41-27.32-17.44s-28.82,5.09-29.39,13.69,11.67,16.41,27.33,17.44,28.81-5.09,29.38-13.69Z" />
        </g>
        <g id="ELLIPSE-18" data-name="ELLIPSE">
          <path class="cls-7"
            d="M1037.15,6172.61c.57-8.6-11.66-16.41-27.32-17.44s-28.82,5.09-29.39,13.69,11.67,16.41,27.33,17.45,28.81-5.1,29.38-13.7Z" />
        </g>
        <g id="LINE-601" data-name="LINE">
          <line class="cls-7" x1="1038.08" y1="6223.74" x2="1038.18" y2="6204.12" />
        </g>
        <g id="SPLINE-31" data-name="SPLINE">
          <path class="cls-7"
            d="M1038.08,6222.7q-.61,9.44,14.32,14.81a45.24,45.24,0,0,0,29.39.91q14.46-4.45,12.91-13.95" />
        </g>
        <g id="SPLINE-32" data-name="SPLINE">
          <path class="cls-7" d="M1094.7,6224.47l.09-18.64" />
        </g>
        <g id="SPLINE-33" data-name="SPLINE">
          <path class="cls-7" d="M980.54,6170.84l-.1,18.58" />
        </g>
        <g id="SPLINE-34" data-name="SPLINE">
          <path class="cls-7" d="M980.44,6189.42q-.63,9.43,14.32,14.81a45.24,45.24,0,0,0,29.39.91q14.46-4.46,12.91-14" />
        </g>
        <g id="SPLINE-35" data-name="SPLINE">
          <path class="cls-7" d="M1037.06,6191.19l.09-18.63" />
        </g>
      </g>
    </g>
    <g id="isla44">
      <g id="LINE-602" data-name="LINE" class="cls-36">
        <polygon class="cls-8"
          points="480.23 6563.17 239.26 6702.29 -0.01 6564.15 0.41 6330.11 38.48 6308.13 480.23 6563.17" />
      </g>
      <g class="cls-61">
        <image loading="lazy" data-clickable="true" data-category-name="el_vertedero" width="95" height="79"
          transform="translate(157.36 6563.61) scale(2.23)" :href="image44" />
      </g>
      <g>
        <g id="LINE-603" data-name="LINE">
          <line class="cls-5" x1="280.29" y1="6469.08" x2="261.59" y2="6458.28" />
        </g>
        <g id="LINE-604" data-name="LINE">
          <line class="cls-5" x1="261.59" y1="6458.28" x2="221.48" y2="6481.44" />
        </g>
        <g id="LINE-605" data-name="LINE">
          <line class="cls-5" x1="221.48" y1="6481.44" x2="240.18" y2="6492.24" />
        </g>
        <g id="LINE-606" data-name="LINE">
          <line class="cls-5" x1="240.18" y1="6492.24" x2="280.29" y2="6469.08" />
        </g>
        <g id="LINE-607" data-name="LINE">
          <line class="cls-5" x1="315.2" y1="6489.24" x2="296.5" y2="6478.44" />
        </g>
        <g id="LINE-608" data-name="LINE">
          <line class="cls-5" x1="296.5" y1="6478.44" x2="256.39" y2="6501.6" />
        </g>
        <g id="LINE-609" data-name="LINE">
          <line class="cls-5" x1="256.39" y1="6501.6" x2="275.09" y2="6512.4" />
        </g>
        <g id="LINE-610" data-name="LINE">
          <line class="cls-5" x1="275.09" y1="6512.4" x2="315.2" y2="6489.24" />
        </g>
        <g id="LINE-611" data-name="LINE">
          <line class="cls-5" x1="350.11" y1="6509.39" x2="331.41" y2="6498.59" />
        </g>
        <g id="LINE-612" data-name="LINE">
          <line class="cls-5" x1="331.41" y1="6498.59" x2="291.3" y2="6521.75" />
        </g>
        <g id="LINE-613" data-name="LINE">
          <line class="cls-5" x1="291.3" y1="6521.75" x2="310" y2="6532.55" />
        </g>
        <g id="LINE-614" data-name="LINE">
          <line class="cls-5" x1="310" y1="6532.55" x2="350.11" y2="6509.39" />
        </g>
        <g id="LINE-615" data-name="LINE">
          <line class="cls-5" x1="385.02" y1="6529.55" x2="366.32" y2="6518.75" />
        </g>
        <g id="LINE-616" data-name="LINE">
          <line class="cls-5" x1="366.32" y1="6518.75" x2="326.21" y2="6541.91" />
        </g>
        <g id="LINE-617" data-name="LINE">
          <line class="cls-5" x1="326.21" y1="6541.91" x2="344.91" y2="6552.71" />
        </g>
        <g id="LINE-618" data-name="LINE">
          <line class="cls-5" x1="344.91" y1="6552.71" x2="385.02" y2="6529.55" />
        </g>
        <g id="LINE-619" data-name="LINE">
          <line class="cls-5" x1="419.93" y1="6549.7" x2="401.23" y2="6538.9" />
        </g>
        <g id="LINE-620" data-name="LINE">
          <line class="cls-5" x1="401.23" y1="6538.9" x2="361.12" y2="6562.06" />
        </g>
        <g id="LINE-621" data-name="LINE">
          <line class="cls-5" x1="361.12" y1="6562.06" x2="379.82" y2="6572.86" />
        </g>
        <g id="LINE-622" data-name="LINE">
          <line class="cls-5" x1="379.82" y1="6572.86" x2="419.93" y2="6549.7" />
        </g>
      </g>
      <g>
        <g id="LINE-623" data-name="LINE">
          <line class="cls-5" x1="156.38" y1="6529.89" x2="137.67" y2="6519.09" />
        </g>
        <g id="LINE-624" data-name="LINE">
          <line class="cls-5" x1="137.67" y1="6519.09" x2="97.56" y2="6542.25" />
        </g>
        <g id="LINE-625" data-name="LINE">
          <line class="cls-5" x1="97.56" y1="6542.25" x2="116.27" y2="6553.05" />
        </g>
        <g id="LINE-626" data-name="LINE">
          <line class="cls-5" x1="116.27" y1="6553.05" x2="156.38" y2="6529.89" />
        </g>
        <g id="LINE-627" data-name="LINE">
          <line class="cls-5" x1="193.59" y1="6551.37" x2="174.88" y2="6540.57" />
        </g>
        <g id="LINE-628" data-name="LINE">
          <line class="cls-5" x1="174.88" y1="6540.57" x2="134.77" y2="6563.73" />
        </g>
        <g id="LINE-629" data-name="LINE">
          <line class="cls-5" x1="134.77" y1="6563.73" x2="153.47" y2="6574.53" />
        </g>
        <g id="LINE-630" data-name="LINE">
          <line class="cls-5" x1="153.47" y1="6574.53" x2="193.59" y2="6551.37" />
        </g>
        <g id="LINE-631" data-name="LINE">
          <line class="cls-5" x1="119.34" y1="6508.5" x2="100.63" y2="6497.7" />
        </g>
        <g id="LINE-632" data-name="LINE">
          <line class="cls-5" x1="100.63" y1="6497.7" x2="60.52" y2="6520.86" />
        </g>
        <g id="LINE-633" data-name="LINE">
          <line class="cls-5" x1="60.52" y1="6520.86" x2="79.23" y2="6531.66" />
        </g>
        <g id="LINE-634" data-name="LINE">
          <line class="cls-5" x1="79.23" y1="6531.66" x2="119.34" y2="6508.5" />
        </g>
        <g id="LINE-635" data-name="LINE">
          <line class="cls-5" x1="31.51" y1="6537.61" x2="50.21" y2="6526.81" />
        </g>
        <g id="LINE-636" data-name="LINE">
          <line class="cls-5" x1="50.21" y1="6526.81" x2="90.33" y2="6549.97" />
        </g>
        <g id="LINE-637" data-name="LINE">
          <line class="cls-5" x1="90.33" y1="6549.97" x2="71.62" y2="6560.77" />
        </g>
        <g id="LINE-638" data-name="LINE">
          <line class="cls-5" x1="71.62" y1="6560.77" x2="31.51" y2="6537.61" />
        </g>
        <g id="LINE-639" data-name="LINE">
          <line class="cls-5" x1="84.35" y1="6568.12" x2="103.06" y2="6557.32" />
        </g>
        <g id="LINE-640" data-name="LINE">
          <line class="cls-5" x1="103.06" y1="6557.32" x2="143.17" y2="6580.48" />
        </g>
        <g id="LINE-641" data-name="LINE">
          <line class="cls-5" x1="143.17" y1="6580.48" x2="124.46" y2="6591.28" />
        </g>
        <g id="LINE-642" data-name="LINE">
          <line class="cls-5" x1="124.46" y1="6591.28" x2="84.35" y2="6568.12" />
        </g>
      </g>
      <g>
        <g id="LINE-643" data-name="LINE">
          <line class="cls-7" x1="240.64" y1="6669.87" x2="240.64" y2="6655.32" />
        </g>
        <g id="LINE-644" data-name="LINE">
          <line class="cls-7" x1="263.19" y1="6627.74" x2="240.64" y2="6655.32" />
        </g>
        <g id="LINE-645" data-name="LINE">
          <line class="cls-7" x1="240.64" y1="6655.32" x2="164.17" y2="6611.17" />
        </g>
        <g id="LINE-646" data-name="LINE">
          <line class="cls-7" x1="164.17" y1="6611.17" x2="186.72" y2="6583.59" />
        </g>
        <g id="LINE-647" data-name="LINE">
          <line class="cls-7" x1="164.17" y1="6611.17" x2="164.17" y2="6625.72" />
        </g>
        <g id="LINE-648" data-name="LINE">
          <line class="cls-7" x1="164.17" y1="6625.72" x2="240.64" y2="6669.87" />
        </g>
        <g id="LINE-649" data-name="LINE">
          <line class="cls-7" x1="240.64" y1="6669.87" x2="303.85" y2="6633.38" />
        </g>
        <g id="LINE-650" data-name="LINE">
          <line class="cls-7" x1="303.85" y1="6633.38" x2="303.85" y2="6618.82" />
        </g>
        <g id="LINE-651" data-name="LINE">
          <line class="cls-7" x1="303.85" y1="6618.82" x2="227.38" y2="6574.67" />
        </g>
        <g id="LINE-652" data-name="LINE">
          <line class="cls-7" x1="227.38" y1="6574.67" x2="186.72" y2="6583.59" />
        </g>
        <g id="LINE-653" data-name="LINE">
          <line class="cls-7" x1="186.72" y1="6583.59" x2="263.19" y2="6627.74" />
        </g>
        <g id="LINE-654" data-name="LINE">
          <line class="cls-7" x1="263.19" y1="6627.74" x2="303.85" y2="6618.82" />
        </g>
      </g>
      <g>
        <g id="SPLINE-36" data-name="SPLINE">
          <path class="cls-7" d="M0,6442.82v61.49" />
        </g>
        <g id="SPLINE-37" data-name="SPLINE">
          <path class="cls-7" d="M0,6504.31q23.9,8,47.08,1.49t23.61-21.35" />
        </g>
        <g id="SPLINE-38" data-name="SPLINE">
          <path class="cls-7" d="M70.68,6484.45q-.86-26.71-23.88-40.27T0,6442.82" />
        </g>
        <g id="SPLINE-39" data-name="SPLINE">
          <path class="cls-7"
            d="M196.88,6445.8q-.72-22.2-19.95-33.31l-16.21-9.36-9-5.18q-18.24-10.53-37.24-1.42t-22.2,29.93" />
        </g>
        <g id="SPLINE-40" data-name="SPLINE">
          <path class="cls-7" d="M92.31,6426.46q-.69,10.44,13.66,17.95" />
        </g>
        <g id="SPLINE-41" data-name="SPLINE">
          <path class="cls-7" d="M106,6444.41l24.08,13.5q18.87,10.58,42.64,6.11t24.17-18.67" />
        </g>
        <g id="SPLINE-42" data-name="SPLINE">
          <path class="cls-7" d="M17.45,6384.52q-.79,12.06,17.89,19.27a61,61,0,0,0,38,2.29q19.26-4.92,19.6-17" />
        </g>
        <g id="SPLINE-43" data-name="SPLINE">
          <path class="cls-7" d="M92.9,6389.08q-1.11-34.58-35.64-36.67t-39.81,32.11" />
        </g>
      </g>
    </g>
    <g id="isla45">
      <g id="LINE-655" data-name="LINE" class="cls-36">
        <polygon class="cls-8" points="859.61 6782.21 -0.01 7278.51 -0.01 6894.5 527.05 6590.21 859.61 6782.21" />
      </g>
      <g class="cls-62">
        <image loading="lazy" data-clickable="true" data-category-name="el_puerto" width="120" height="108"
          transform="translate(571.61 6629.5) scale(2.23)" :href="image45" />
      </g>
      <g>
        <g id="LINE-656" data-name="LINE">
          <line class="cls-5" x1="502.06" y1="6630.95" x2="582.53" y2="6677.4" />
        </g>
        <g id="LINE-657" data-name="LINE">
          <line class="cls-5" x1="582.53" y1="6677.4" x2="560.47" y2="6690.14" />
        </g>
        <g id="LINE-658" data-name="LINE">
          <line class="cls-5" x1="560.47" y1="6690.14" x2="480" y2="6643.68" />
        </g>
        <g id="LINE-659" data-name="LINE">
          <line class="cls-5" x1="480" y1="6643.68" x2="502.06" y2="6630.95" />
        </g>
        <g id="LINE-660" data-name="LINE">
          <line class="cls-5" x1="462.98" y1="6653.51" x2="543.45" y2="6699.97" />
        </g>
        <g id="LINE-661" data-name="LINE">
          <line class="cls-5" x1="543.45" y1="6699.97" x2="521.39" y2="6712.71" />
        </g>
        <g id="LINE-662" data-name="LINE">
          <line class="cls-5" x1="521.39" y1="6712.71" x2="440.92" y2="6666.25" />
        </g>
        <g id="LINE-663" data-name="LINE">
          <line class="cls-5" x1="440.92" y1="6666.25" x2="462.98" y2="6653.51" />
        </g>
        <g id="LINE-664" data-name="LINE">
          <line class="cls-5" x1="423.9" y1="6676.08" x2="504.36" y2="6722.53" />
        </g>
        <g id="LINE-665" data-name="LINE">
          <line class="cls-5" x1="504.36" y1="6722.53" x2="482.3" y2="6735.27" />
        </g>
        <g id="LINE-666" data-name="LINE">
          <line class="cls-5" x1="482.3" y1="6735.27" x2="401.83" y2="6688.81" />
        </g>
        <g id="LINE-667" data-name="LINE">
          <line class="cls-5" x1="401.83" y1="6688.81" x2="423.9" y2="6676.08" />
        </g>
        <g id="LINE-668" data-name="LINE">
          <line class="cls-5" x1="384.81" y1="6698.64" x2="465.28" y2="6745.1" />
        </g>
        <g id="LINE-669" data-name="LINE">
          <line class="cls-5" x1="465.28" y1="6745.1" x2="443.22" y2="6757.84" />
        </g>
        <g id="LINE-670" data-name="LINE">
          <line class="cls-5" x1="443.22" y1="6757.84" x2="362.75" y2="6711.38" />
        </g>
        <g id="LINE-671" data-name="LINE">
          <line class="cls-5" x1="362.75" y1="6711.38" x2="384.81" y2="6698.64" />
        </g>
        <g id="LINE-672" data-name="LINE">
          <line class="cls-5" x1="345.73" y1="6721.2" x2="426.2" y2="6767.66" />
        </g>
        <g id="LINE-673" data-name="LINE">
          <line class="cls-5" x1="426.2" y1="6767.66" x2="404.14" y2="6780.4" />
        </g>
        <g id="LINE-674" data-name="LINE">
          <line class="cls-5" x1="404.14" y1="6780.4" x2="323.67" y2="6733.94" />
        </g>
        <g id="LINE-675" data-name="LINE">
          <line class="cls-5" x1="323.67" y1="6733.94" x2="345.73" y2="6721.2" />
        </g>
        <g id="LINE-676" data-name="LINE">
          <line class="cls-5" x1="263.82" y1="6768.49" x2="344.29" y2="6814.95" />
        </g>
        <g id="LINE-677" data-name="LINE">
          <line class="cls-5" x1="344.29" y1="6814.95" x2="322.23" y2="6827.69" />
        </g>
        <g id="LINE-678" data-name="LINE">
          <line class="cls-5" x1="322.23" y1="6827.69" x2="241.76" y2="6781.23" />
        </g>
        <g id="LINE-679" data-name="LINE">
          <line class="cls-5" x1="241.76" y1="6781.23" x2="263.82" y2="6768.49" />
        </g>
        <g id="LINE-680" data-name="LINE">
          <line class="cls-5" x1="224.74" y1="6791.06" x2="305.21" y2="6837.52" />
        </g>
        <g id="LINE-681" data-name="LINE">
          <line class="cls-5" x1="305.21" y1="6837.52" x2="283.14" y2="6850.26" />
        </g>
        <g id="LINE-682" data-name="LINE">
          <line class="cls-5" x1="283.14" y1="6850.26" x2="202.67" y2="6803.8" />
        </g>
        <g id="LINE-683" data-name="LINE">
          <line class="cls-5" x1="202.67" y1="6803.8" x2="224.74" y2="6791.06" />
        </g>
        <g id="LINE-684" data-name="LINE">
          <line class="cls-5" x1="185.65" y1="6813.62" x2="266.12" y2="6860.08" />
        </g>
        <g id="LINE-685" data-name="LINE">
          <line class="cls-5" x1="266.12" y1="6860.08" x2="244.06" y2="6872.82" />
        </g>
        <g id="LINE-686" data-name="LINE">
          <line class="cls-5" x1="244.06" y1="6872.82" x2="163.59" y2="6826.36" />
        </g>
        <g id="LINE-687" data-name="LINE">
          <line class="cls-5" x1="163.59" y1="6826.36" x2="185.65" y2="6813.62" />
        </g>
        <g id="LINE-688" data-name="LINE">
          <line class="cls-5" x1="146.57" y1="6836.19" x2="227.04" y2="6882.65" />
        </g>
        <g id="LINE-689" data-name="LINE">
          <line class="cls-5" x1="227.04" y1="6882.65" x2="204.98" y2="6895.38" />
        </g>
        <g id="LINE-690" data-name="LINE">
          <line class="cls-5" x1="204.98" y1="6895.38" x2="124.51" y2="6848.93" />
        </g>
        <g id="LINE-691" data-name="LINE">
          <line class="cls-5" x1="124.51" y1="6848.93" x2="146.57" y2="6836.19" />
        </g>
        <g id="LINE-692" data-name="LINE">
          <line class="cls-5" x1="107.49" y1="6858.75" x2="187.96" y2="6905.21" />
        </g>
        <g id="LINE-693" data-name="LINE">
          <line class="cls-5" x1="187.96" y1="6905.21" x2="165.89" y2="6917.95" />
        </g>
        <g id="LINE-694" data-name="LINE">
          <line class="cls-5" x1="165.89" y1="6917.95" x2="85.43" y2="6871.49" />
        </g>
        <g id="LINE-695" data-name="LINE">
          <line class="cls-5" x1="85.43" y1="6871.49" x2="107.49" y2="6858.75" />
        </g>
        <g id="LINE-696" data-name="LINE">
          <line class="cls-5" x1="25.58" y1="6906.04" x2="106.05" y2="6952.5" />
        </g>
        <g id="LINE-697" data-name="LINE">
          <line class="cls-5" x1="106.05" y1="6952.5" x2="83.99" y2="6965.24" />
        </g>
        <g id="LINE-698" data-name="LINE">
          <line class="cls-5" x1="83.99" y1="6965.24" x2="3.52" y2="6918.78" />
        </g>
        <g id="LINE-699" data-name="LINE">
          <line class="cls-5" x1="3.52" y1="6918.78" x2="25.58" y2="6906.04" />
        </g>
        <g id="LINE-700" data-name="LINE">
          <line class="cls-5" x1="547.83" y1="6762.83" x2="338.78" y2="6883.52" />
        </g>
        <g id="LINE-701" data-name="LINE">
          <line class="cls-5" x1="338.78" y1="6883.52" x2="360.85" y2="6896.26" />
        </g>
        <g id="LINE-702" data-name="LINE">
          <line class="cls-5" x1="360.85" y1="6896.26" x2="569.89" y2="6775.57" />
        </g>
        <g id="LINE-703" data-name="LINE">
          <line class="cls-5" x1="569.89" y1="6775.57" x2="547.83" y2="6762.83" />
        </g>
        <g id="LINE-704" data-name="LINE">
          <line class="cls-5" x1="586.91" y1="6785.39" x2="377.87" y2="6906.09" />
        </g>
        <g id="LINE-705" data-name="LINE">
          <line class="cls-5" x1="377.87" y1="6906.09" x2="399.93" y2="6918.82" />
        </g>
        <g id="LINE-706" data-name="LINE">
          <line class="cls-5" x1="399.93" y1="6918.82" x2="608.98" y2="6798.13" />
        </g>
        <g id="LINE-707" data-name="LINE">
          <line class="cls-5" x1="608.98" y1="6798.13" x2="586.91" y2="6785.39" />
        </g>
        <g id="LINE-708" data-name="LINE">
          <line class="cls-5" x1="626" y1="6807.96" x2="416.95" y2="6928.65" />
        </g>
        <g id="LINE-709" data-name="LINE">
          <line class="cls-5" x1="416.95" y1="6928.65" x2="439.01" y2="6941.39" />
        </g>
        <g id="LINE-710" data-name="LINE">
          <line class="cls-5" x1="439.01" y1="6941.39" x2="648.06" y2="6820.7" />
        </g>
        <g id="LINE-711" data-name="LINE">
          <line class="cls-5" x1="648.06" y1="6820.7" x2="626" y2="6807.96" />
        </g>
        <g id="LINE-712" data-name="LINE">
          <line class="cls-5" x1="665.08" y1="6830.52" x2="456.03" y2="6951.22" />
        </g>
        <g id="LINE-713" data-name="LINE">
          <line class="cls-5" x1="456.03" y1="6951.22" x2="478.09" y2="6963.95" />
        </g>
        <g id="LINE-714" data-name="LINE">
          <line class="cls-5" x1="478.09" y1="6963.95" x2="687.14" y2="6843.26" />
        </g>
        <g id="LINE-715" data-name="LINE">
          <line class="cls-5" x1="687.14" y1="6843.26" x2="665.08" y2="6830.52" />
        </g>
        <g id="LINE-716" data-name="LINE">
          <line class="cls-5" x1="283.54" y1="6910.14" x2="74.49" y2="7030.83" />
        </g>
        <g id="LINE-717" data-name="LINE">
          <line class="cls-5" x1="74.49" y1="7030.83" x2="96.56" y2="7043.57" />
        </g>
        <g id="LINE-718" data-name="LINE">
          <line class="cls-5" x1="96.56" y1="7043.57" x2="305.6" y2="6922.87" />
        </g>
        <g id="LINE-719" data-name="LINE">
          <line class="cls-5" x1="305.6" y1="6922.87" x2="283.54" y2="6910.14" />
        </g>
        <g id="LINE-720" data-name="LINE">
          <line class="cls-5" x1="322.62" y1="6932.7" x2="113.58" y2="7053.39" />
        </g>
        <g id="LINE-721" data-name="LINE">
          <line class="cls-5" x1="113.58" y1="7053.39" x2="135.64" y2="7066.13" />
        </g>
        <g id="LINE-722" data-name="LINE">
          <line class="cls-5" x1="135.64" y1="7066.13" x2="344.68" y2="6945.44" />
        </g>
        <g id="LINE-723" data-name="LINE">
          <line class="cls-5" x1="344.68" y1="6945.44" x2="322.62" y2="6932.7" />
        </g>
        <g id="LINE-724" data-name="LINE">
          <line class="cls-5" x1="361.71" y1="6955.27" x2="152.66" y2="7075.96" />
        </g>
        <g id="LINE-725" data-name="LINE">
          <line class="cls-5" x1="152.66" y1="7075.96" x2="174.72" y2="7088.7" />
        </g>
        <g id="LINE-726" data-name="LINE">
          <line class="cls-5" x1="174.72" y1="7088.7" x2="383.77" y2="6968" />
        </g>
        <g id="LINE-727" data-name="LINE">
          <line class="cls-5" x1="383.77" y1="6968" x2="361.71" y2="6955.27" />
        </g>
        <g id="LINE-728" data-name="LINE">
          <line class="cls-5" x1="400.79" y1="6977.83" x2="191.74" y2="7098.52" />
        </g>
        <g id="LINE-729" data-name="LINE">
          <line class="cls-5" x1="191.74" y1="7098.52" x2="213.8" y2="7111.26" />
        </g>
        <g id="LINE-730" data-name="LINE">
          <line class="cls-5" x1="213.8" y1="7111.26" x2="422.85" y2="6990.57" />
        </g>
        <g id="LINE-731" data-name="LINE">
          <line class="cls-5" x1="422.85" y1="6990.57" x2="400.79" y2="6977.83" />
        </g>
        <g id="LINE-732" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="7007.01" x2="5.82" y2="7010.37" />
        </g>
        <g id="LINE-733" data-name="LINE">
          <line class="cls-5" x1="5.82" y1="7010.37" x2="27.88" y2="6997.63" />
        </g>
        <g id="LINE-734" data-name="LINE">
          <line class="cls-5" x1="27.88" y1="6997.63" x2="-0.01" y2="6981.53" />
        </g>
        <g id="LINE-735" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="6936.4" x2="66.96" y2="6975.07" />
        </g>
        <g id="LINE-736" data-name="LINE">
          <line class="cls-5" x1="66.96" y1="6975.07" x2="44.9" y2="6987.8" />
        </g>
        <g id="LINE-737" data-name="LINE">
          <line class="cls-5" x1="44.9" y1="6987.8" x2="-0.01" y2="6961.88" />
        </g>
        <g id="LINE-738" data-name="LINE">
          <line class="cls-5" x1="19.25" y1="7057.44" x2="-0.01" y2="7068.56" />
        </g>
        <g id="LINE-739" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="7094.04" x2="41.31" y2="7070.18" />
        </g>
        <g id="LINE-740" data-name="LINE">
          <line class="cls-5" x1="41.31" y1="7070.18" x2="19.25" y2="7057.44" />
        </g>
        <g id="LINE-741" data-name="LINE">
          <line class="cls-5" x1="58.33" y1="7080.01" x2="-0.01" y2="7113.69" />
        </g>
        <g id="LINE-742" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="7139.17" x2="80.39" y2="7092.75" />
        </g>
        <g id="LINE-743" data-name="LINE">
          <line class="cls-5" x1="80.39" y1="7092.75" x2="58.33" y2="7080.01" />
        </g>
        <g id="LINE-744" data-name="LINE">
          <line class="cls-5" x1="97.42" y1="7102.57" x2="-0.01" y2="7158.82" />
        </g>
        <g id="LINE-745" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="7184.3" x2="119.48" y2="7115.31" />
        </g>
        <g id="LINE-746" data-name="LINE">
          <line class="cls-5" x1="119.48" y1="7115.31" x2="97.42" y2="7102.57" />
        </g>
        <g id="LINE-747" data-name="LINE">
          <line class="cls-5" x1="136.5" y1="7125.14" x2="-0.01" y2="7203.95" />
        </g>
        <g id="LINE-748" data-name="LINE">
          <line class="cls-5" x1="-0.01" y1="7229.42" x2="158.56" y2="7137.88" />
        </g>
        <g id="LINE-749" data-name="LINE">
          <line class="cls-5" x1="158.56" y1="7137.88" x2="136.5" y2="7125.14" />
        </g>
      </g>
      <g>
        <g id="LINE-750" data-name="LINE">
          <line class="cls-7" x1="735.96" y1="6827.39" x2="735.96" y2="6804.88" />
        </g>
        <g id="LINE-751" data-name="LINE">
          <line class="cls-7" x1="735.96" y1="6804.88" x2="792.54" y2="6756.19" />
        </g>
        <g id="LINE-752" data-name="LINE">
          <line class="cls-7" x1="792.54" y1="6794.73" x2="792.54" y2="6756.19" />
        </g>
        <g id="LINE-753" data-name="LINE">
          <line class="cls-7" x1="735.96" y1="6804.88" x2="604.79" y2="6729.15" />
        </g>
        <g id="LINE-754" data-name="LINE">
          <line class="cls-7" x1="661.37" y1="6680.46" x2="792.54" y2="6756.19" />
        </g>
        <g id="LINE-755" data-name="LINE">
          <line class="cls-7" x1="792.54" y1="6756.19" x2="792.54" y2="6794.73" />
        </g>
        <g id="LINE-756" data-name="LINE">
          <line class="cls-7" x1="792.54" y1="6794.73" x2="735.96" y2="6827.39" />
        </g>
        <g id="LINE-757" data-name="LINE">
          <line class="cls-7" x1="735.96" y1="6827.39" x2="604.79" y2="6751.66" />
        </g>
        <g id="LINE-758" data-name="LINE">
          <line class="cls-7" x1="604.79" y1="6751.66" x2="604.79" y2="6729.15" />
        </g>
        <g id="LINE-759" data-name="LINE">
          <line class="cls-7" x1="604.79" y1="6729.15" x2="661.37" y2="6680.46" />
        </g>
      </g>
    </g>
    <g id="isla46">
      <g class="cls-63">
        <image loading="lazy" data-clickable="true" data-category-name="el_mar" width="495" height="723"
          transform="translate(2.27 5984.01) scale(2.27)" :href="image46" />
      </g>
      <g id="LWPOLYLINE-48" data-name="LWPOLYLINE">
        <polygon class="cls-7"
          points="1125.01 6635.5 1125.01 7625 0.01 7625 0.01 7379.28 1015.59 6792.94 0.01 6206.59 0.01 5985.98 1125.01 6635.5" />
      </g>
    </g>
    <g id="etiquetes">
      <rect class="cls-64" x="308.47" y="483.28" width="167" height="33.4" />
      <text class="cls-65" transform="translate(315.76 502.59)">
        los jardines
      </text>
      <line class="cls-66" x1="308.47" y1="483.28" x2="308.47" y2="566.78" />
      <circle class="cls-67" cx="307.59" cy="566.78" r="5.27" />
      <rect class="cls-64" x="736.36" y="386.05" width="160.98" height="33.4" />
      <text class="cls-65" transform="translate(743.66 405.36)">
        el mercado
      </text>
      <line class="cls-66" x1="896.33" y1="386.05" x2="896.33" y2="469.55" />
      <circle class="cls-67" cx="895.45" cy="469.55" r="5.27" />
      <rect class="cls-64" x="347.24" y="672.99" width="160.98" height="33.4" />
      <text class="cls-65" transform="translate(354.53 692.31)">
        la farmacia
      </text>
      <line class="cls-66" x1="508.96" y1="672.99" x2="508.96" y2="756.49" />
      <circle class="cls-67" cx="508.09" cy="756.49" r="5.27" />
      <rect class="cls-68" x="765.51" y="827.91" width="132.96" height="33.4" />
      <text class="cls-65" transform="translate(774.66 847.22)">el banco</text>
      <line class="cls-66" x1="897.45" y1="827.91" x2="897.45" y2="911.41" />
      <circle class="cls-67" cx="896.57" cy="911.41" r="5.27" />
      <rect class="cls-68" x="313.87" y="876.05" width="189.72" height="60.76" />
      <line class="cls-66" x1="313.87" y1="876.05" x2="313.87" y2="959.55" />
      <circle class="cls-67" cx="312.99" cy="959.55" r="5.27" />
      <text class="cls-65" transform="translate(327.43 895.59)">
        la residencia
        <tspan x="0" y="26.37">de ancianos</tspan>
      </text>
      <rect class="cls-69" x="185.23" y="1157.28" width="51.49" height="33.4" />
      <line class="cls-66" x1="185.23" y1="1157.28" x2="185.23" y2="1240.78" />
      <circle class="cls-67" cx="184.35" cy="1240.78" r="5.27" />
      <rect class="cls-69" x="781.33" y="1212.55" width="187.95" height="33.4" />
      <text class="cls-65" transform="translate(790.98 1231.86)">
        el prostíbulo
      </text>
      <line class="cls-66" x1="968.26" y1="1212.55" x2="968.26" y2="1296.04" />
      <circle class="cls-67" cx="967.38" cy="1296.04" r="5.27" />
      <rect class="cls-69" x="546.43" y="1368.4" width="103.06" height="33.4" />
      <line class="cls-66" x1="546.43" y1="1368.4" x2="546.43" y2="1451.89" />
      <circle class="cls-67" cx="545.55" cy="1451.89" r="5.27" />
      <text class="cls-65" transform="translate(554.72 1387.94)">el cine</text>
      <rect class="cls-69" x="199.92" y="1599.99" width="198.2" height="33.4" />
      <text class="cls-65" transform="translate(207.21 1619.3)">
        la universidad
      </text>
      <line class="cls-66" x1="199.92" y1="1599.99" x2="199.92" y2="1683.49" />
      <circle class="cls-67" cx="199.04" cy="1683.49" r="5.27" />
      <rect class="cls-69" x="543.15" y="1533.04" width="145.01" height="33.4" />
      <text class="cls-65" transform="translate(550.44 1552.35)">
        la escuela
      </text>
      <line class="cls-66" x1="543.15" y1="1533.04" x2="543.15" y2="1616.54" />
      <circle class="cls-67" cx="542.27" cy="1616.54" r="5.27" />
      <rect class="cls-68" x="754.32" y="1867.28" width="147.67" height="33.4" />
      <text class="cls-65" transform="translate(761.91 1885.59)">
        el parking
      </text>
      <line class="cls-66" x1="901.99" y1="1867.28" x2="901.99" y2="1950.78" />
      <circle class="cls-67" cx="901.11" cy="1950.78" r="5.27" />
      <rect class="cls-68" x="329.31" y="1897.26" width="197.38" height="33.4" />
      <text class="cls-65" transform="translate(336.6 1916.57)">
        la inmobiliaria
      </text>
      <line class="cls-66" x1="329.31" y1="1897.26" x2="329.31" y2="1980.76" />
      <circle class="cls-67" cx="328.43" cy="1980.76" r="5.27" />
      <rect class="cls-68" x="450.71" y="2006.88" width="118.27" height="33.4" />
      <text class="cls-65" transform="translate(460.54 2026.19)">el hotel</text>
      <line class="cls-66" x1="568.98" y1="2006.88" x2="568.98" y2="2090.38" />
      <circle class="cls-67" cx="568.1" cy="2090.38" r="5.27" />
      <rect class="cls-68" x="846.96" y="2062.24" width="115.31" height="33.4" />
      <text class="cls-65" transform="translate(854.26 2081.55)">la bolsa</text>
      <line class="cls-66" x1="846.96" y1="2062.24" x2="846.96" y2="2145.74" />
      <circle class="cls-67" cx="846.09" cy="2145.74" r="5.27" />
      <rect class="cls-68" x="148.7" y="2199.71" width="157.31" height="33.4" />
      <text class="cls-65" transform="translate(158.93 2219.03)">
        el hospital
      </text>
      <line class="cls-66" x1="306.01" y1="2199.71" x2="306.01" y2="2283.21" />
      <circle class="cls-67" cx="305.13" cy="2283.21" r="5.27" />
      <rect class="cls-68" x="497.56" y="2281.64" width="140.13" height="33.4" />
      <text class="cls-65" transform="translate(507.6 2300.95)">el museo</text>
      <line class="cls-66" x1="637.68" y1="2281.64" x2="637.68" y2="2365.14" />
      <circle class="cls-67" cx="636.8" cy="2365.14" r="5.27" />
      <rect class="cls-68" x="768.19" y="2337.31" width="165.61" height="33.4" />
      <text class="cls-65" transform="translate(778.72 2356.62)">
        el instituto
      </text>
      <line class="cls-66" x1="933.8" y1="2337.31" x2="933.8" y2="2420.81" />
      <circle class="cls-67" cx="932.92" cy="2420.81" r="5.27" />
      <rect class="cls-68" x="149.53" y="2354.06" width="188.84" height="33.4" />
      <text class="cls-65" transform="translate(156.82 2373.37)">
        el veterinario
      </text>
      <line class="cls-66" x1="149.53" y1="2354.06" x2="149.53" y2="2437.56" />
      <circle class="cls-67" cx="148.65" cy="2437.56" r="5.27" />
      <rect class="cls-68" x="324.34" y="2521.99" width="143.9" height="59.01" />
      <text class="cls-65" transform="translate(335.16 2541.3)">
        el club
        <tspan x="0" y="27">de fútbol</tspan>
      </text>
      <line class="cls-66" x1="468.24" y1="2521.99" x2="468.24" y2="2605.49" />
      <circle class="cls-67" cx="467.36" cy="2605.49" r="5.27" />
      <rect class="cls-68" x="179.64" y="2642.48" width="128.45" height="33.4" />
      <text class="cls-65" transform="translate(186.93 2661.79)">
        el teatro
      </text>
      <line class="cls-66" x1="179.64" y1="2642.48" x2="179.64" y2="2725.98" />
      <circle class="cls-67" cx="178.76" cy="2725.98" r="5.27" />
      <rect class="cls-68" x="221.43" y="2987.78" width="231.95" height="33.4" />
      <text class="cls-65" transform="translate(228.72 3007.09)">
        el huerto urbano
      </text>
      <line class="cls-66" x1="221.43" y1="2987.78" x2="221.43" y2="3071.28" />
      <circle class="cls-67" cx="220.55" cy="3071.28" r="5.27" />
      <rect class="cls-68" x="792.47" y="3187.22" width="197.38" height="33.4" />
      <text class="cls-65" transform="translate(799.77 3206.53)">
        los bomberos
      </text>
      <line class="cls-66" x1="792.47" y1="3187.22" x2="792.47" y2="3270.72" />
      <circle class="cls-67" cx="791.59" cy="3270.72" r="5.27" />
      <rect class="cls-68" x="861.89" y="2759.08" width="87.51" height="33.4" />
      <text class="cls-65" transform="translate(873.32 2778.39)">el río</text>
      <line class="cls-66" x1="949.4" y1="2759.08" x2="949.4" y2="2842.58" />
      <circle class="cls-67" cx="948.53" cy="2842.58" r="5.27" />
      <rect class="cls-68" x="450.92" y="3400.33" width="177.39" height="33.4" />
      <text class="cls-65" transform="translate(458.21 3419.65)">
        la discoteca
      </text>
      <line class="cls-66" x1="450.92" y1="3400.33" x2="450.92" y2="3483.83" />
      <circle class="cls-67" cx="450.04" cy="3483.83" r="5.27" />
      <rect class="cls-68" x="558.19" y="929.99" width="225.58" height="33.4" />
      <text class="cls-65" transform="translate(565.48 949.3)">
        el ayuntamiento
      </text>
      <line class="cls-66" x1="558.19" y1="929.99" x2="558.19" y2="1013.49" />
      <circle class="cls-67" cx="557.31" cy="1013.49" r="5.27" />
      <rect class="cls-68" x="587.79" y="3612.57" width="227.38" height="33.4" />
      <text class="cls-65" transform="translate(591.09 3631.88)">
        el supermercado
      </text>
      <line class="cls-66" x1="815.17" y1="3612.57" x2="815.17" y2="3696.07" />
      <circle class="cls-67" cx="814.29" cy="3696.07" r="5.27" />
      <rect class="cls-68" x="355.68" y="3809.4" width="217.6" height="33.4" />
      <text class="cls-65" transform="translate(363.2 3828.71)">
        el observatorio
      </text>
      <line class="cls-66" x1="573.28" y1="3809.4" x2="573.28" y2="3892.9" />
      <circle class="cls-67" cx="572.41" cy="3892.9" r="5.27" />
      <rect class="cls-68" x="738.76" y="3902.96" width="164.89" height="33.4" />
      <text class="cls-65" transform="translate(748.57 3922.27)">
        la empresa
      </text>
      <line class="cls-66" x1="903.66" y1="3902.96" x2="903.66" y2="3986.46" />
      <circle class="cls-67" cx="902.78" cy="3986.46" r="5.27" />
      <rect class="cls-68" x="360.16" y="4099.8" width="226.46" height="33.4" />
      <text class="cls-65" transform="translate(370.54 4119.11)">
        una comunidad
      </text>
      <line class="cls-66" x1="586.62" y1="4099.8" x2="586.62" y2="4183.29" />
      <circle class="cls-67" cx="585.74" cy="4183.29" r="5.27" />
      <rect class="cls-68" x="142.6" y="4000.7" width="197.38" height="33.4" />
      <text class="cls-65" transform="translate(149.89 4020.01)">
        el manicomio
      </text>
      <line class="cls-66" x1="142.6" y1="4000.7" x2="142.6" y2="4084.19" />
      <circle class="cls-67" cx="141.72" cy="4084.19" r="5.27" />
      <rect class="cls-68" x="407.39" y="4188.87" width="171.78" height="33.4" />
      <text class="cls-65" transform="translate(414.68 4208.18)">
        la televisión
      </text>
      <line class="cls-66" x1="407.39" y1="4188.87" x2="407.39" y2="4272.36" />
      <circle class="cls-67" cx="406.51" cy="4272.36" r="5.27" />
      <rect class="cls-68" x="840.96" y="4301.65" width="141.53" height="33.4" />
      <text class="cls-65" transform="translate(852.41 4320.96)">
        la policía
      </text>
      <line class="cls-66" x1="982.49" y1="4301.65" x2="982.49" y2="4385.15" />
      <circle class="cls-67" cx="981.61" cy="4385.15" r="5.27" />
      <rect class="cls-68" x="604.02" y="4517.93" width="164.72" height="33.4" />
      <text class="cls-65" transform="translate(617.66 4537.24)">
        la estación
      </text>
      <text class="cls-70" transform="translate(768.75 4538.78) rotate(90)">
        L
        <tspan x="12.03" y="0">o</tspan>
        <tspan x="24.01" y="0">r</tspan>
        <tspan x="36.01" y="0">e</tspan>
      </text>
      <circle class="cls-67" cx="767.87" cy="4601.43" r="5.27" />
      <rect class="cls-68" x="798.04" y="4935.54" width="139.25" height="59.76" />
      <text class="cls-65" transform="translate(806.21 4954.85)">
        el cuartel
        <tspan x="0" y="27">militar</tspan>
      </text>
      <line class="cls-66" x1="937.3" y1="4935.54" x2="937.3" y2="5019.04" />
      <circle class="cls-67" cx="936.42" cy="5019.04" r="5.27" />
      <rect class="cls-68" x="255.39" y="4668.29" width="125.64" height="33.4" />
      <text class="cls-65" transform="translate(262.68 4687.6)">la cárcel</text>
      <line class="cls-66" x1="255.39" y1="4668.29" x2="255.39" y2="4751.79" />
      <circle class="cls-67" cx="254.51" cy="4751.79" r="5.27" />
      <rect class="cls-68" x="396.26" y="4746.19" width="200.95" height="33.4" />
      <line class="cls-66" x1="396.26" y1="4746.19" x2="396.26" y2="4829.68" />
      <circle class="cls-67" cx="395.38" cy="4829.68" r="5.27" />
      <rect class="cls-68" x="659.3" y="4889.82" width="172.29" height="33.4" />
      <text class="cls-65" transform="translate(666.59 4909.13)">
        la guardería
      </text>
      <line class="cls-66" x1="659.3" y1="4889.82" x2="659.3" y2="4973.32" />
      <circle class="cls-67" cx="658.42" cy="4973.32" r="5.27" />
      <rect class="cls-68" x="213.67" y="5062.37" width="127.63" height="56.4" />
      <text class="cls-65" transform="translate(220.97 5081.68)">
        la plaza
        <tspan x="0" y="24">de toros</tspan>
      </text>
      <line class="cls-66" x1="213.67" y1="5062.37" x2="213.67" y2="5145.87" />
      <circle class="cls-67" cx="212.79" cy="5145.87" r="5.27" />
      <rect class="cls-68" x="822.49" y="5385.51" width="197.38" height="33.4" />
      <text class="cls-65" transform="translate(829.78 5404.83)">
        el cementerio
      </text>
      <line class="cls-66" x1="822.49" y1="5385.51" x2="822.49" y2="5469.01" />
      <circle class="cls-67" cx="821.61" cy="5469.01" r="5.27" />
      <rect class="cls-68" x="745.87" y="5643.59" width="96.62" height="33.4" />
      <text class="cls-65" transform="translate(755.41 5662.9)">el zoo</text>
      <line class="cls-66" x1="842.49" y1="5643.59" x2="842.49" y2="5727.09" />
      <circle class="cls-67" cx="841.61" cy="5727.09" r="5.27" />
      <rect class="cls-68" x="442.31" y="5870.4" width="145.95" height="60.04" />
      <text class="cls-65" transform="translate(455.17 5889.71)">
        la central
        <tspan x="0" y="26.53">eléctrica</tspan>
      </text>
      <line class="cls-66" x1="588.26" y1="5870.4" x2="588.26" y2="5953.9" />
      <circle class="cls-67" cx="587.38" cy="5953.9" r="5.27" />
      <rect class="cls-68" x="346.83" y="5704.89" width="126.73" height="33.4" />
      <text class="cls-65" transform="translate(354.13 5724.2)">la granja</text>
      <line class="cls-66" x1="346.83" y1="5704.89" x2="346.83" y2="5788.39" />
      <circle class="cls-67" cx="345.95" cy="5788.39" r="5.27" />
      <rect class="cls-68" x="580.36" y="6237.21" width="100.76" height="33.4" />
      <text class="cls-65" transform="translate(587.66 6256.52)">el mar</text>
      <line class="cls-66" x1="580.36" y1="6237.21" x2="580.36" y2="6320.71" />
      <circle class="cls-67" cx="579.49" cy="6320.71" r="5.27" />
      <rect class="cls-68" x="187.68" y="6499.86" width="175.32" height="33.4" />
      <text class="cls-65" transform="translate(194.97 6519.17)">
        el vertedero
      </text>
      <line class="cls-66" x1="187.68" y1="6499.86" x2="187.68" y2="6583.36" />
      <circle class="cls-67" cx="186.8" cy="6583.36" r="5.27" />
      <rect class="cls-68" x="468.19" y="6644.97" width="137.02" height="33.4" />
      <text class="cls-65" transform="translate(477.13 6664.28)">
        el puerto
      </text>
      <line class="cls-66" x1="605.21" y1="6644.97" x2="605.21" y2="6728.47" />
      <circle class="cls-67" cx="604.33" cy="6728.47" r="5.27" />
      <rect class="cls-68" x="834.18" y="3323.18" width="155.79" height="33.4" />
      <text class="cls-65" transform="translate(844.89 3342.49)">
        el tribunal
      </text>
      <line class="cls-66" x1="989.98" y1="3323.18" x2="989.98" y2="3406.68" />
      <circle class="cls-67" cx="989.1" cy="3406.68" r="5.27" />
      <rect class="cls-68" x="754.26" y="6118.48" width="197.38" height="33.4" />
      <text class="cls-65" transform="translate(761.55 6137.79)">
        la depuradora
      </text>
      <line class="cls-66" x1="951.64" y1="6118.48" x2="951.64" y2="6201.98" />
      <circle class="cls-67" cx="950.76" cy="6201.98" r="5.27" />
      <line class="cls-66" x1="769.09" y1="4517.65" x2="769.09" y2="4601.15" />
      <rect class="cls-68" x="129.51" y="3581.99" width="198.21" height="33.4" />
      <line class="cls-66" x1="129.51" y1="3581.99" x2="129.51" y2="3665.49" />
      <circle class="cls-67" cx="128.63" cy="3665.49" r="5.27" />
      <text class="cls-65" transform="translate(137.79 3601.53)">
        el parlamento
      </text>
      <text class="cls-65" transform="translate(196.72 1175.31)">¿?</text>
      <text class="cls-65" transform="translate(405.52 4765.79)">
        el restaurante
      </text>
      <rect class="cls-68" x="788.88" y="1551.53" width="193.82" height="59.28" />
      <text class="cls-65" transform="translate(796.17 1570.84)">
        el centro de
        <tspan x="0" y="25">computación</tspan>
      </text>
      <line class="cls-66" x1="788.88" y1="1551.53" x2="788.88" y2="1675.03" />
      <circle class="cls-67" cx="788" cy="1675.03" r="5.27" />
      <rect class="cls-69" x="146.15" y="4364.72" width="91.08" height="33.4" />
      <text class="cls-65" transform="translate(153.44 4384.03)">la aso</text>
      <line class="cls-66" x1="146.15" y1="4364.72" x2="146.15" y2="4448.22" />
      <circle class="cls-67" cx="145.27" cy="4448.22" r="5.27" />
    </g>
  </svg>
</template>
<style scoped>
svg {
  top: -100px;
  position: absolute;
  fill: var(--black);
}

@keyframes shake {
  from {
    transform: translateX(-10);
  }

  to {
    transform: translateX(10);
  }
}

[data-clickable="true"] {
  cursor: pointer;
  border: solid 1px red;
  transition: all 0.3s ease;
}

[data-clickable="true"]:hover,
[data-clickable="false"] {
  filter: grayscale(100%);
}

.el_prostibulo__image {
  clip-path: url("#clip-path__el_prostibulo");
}

.el_tribunal__image {
  clip-path: url("#clip-path__el_tribunal");
}

.la_television__image {
  clip-path: url("#clip-path__la_television");
}

.la_estacion__image {
  clip-path: url("#clip-path__la_estacion");
}

.illustration-container {
  position: relative;
}

#etiquetes text {
  font-family: "Schibsted Grotesk", serif !important;
}
</style>
<style scoped>
.cls-1,
.cls-11,
.cls-15,
.cls-18,
.cls-5,
.cls-56,
.cls-57,
.cls-6,
.cls-66,
.cls-7 {
  fill: none;
}

.cls-11,
.cls-18,
.cls-2 {
  stroke: #000;
}

.cls-11,
.cls-18,
.cls-19,
.cls-2,
.cls-5,
.cls-57,
.cls-6,
.cls-7,
.cls-8 {
  stroke-linecap: round;
}

.cls-11,
.cls-18,
.cls-19,
.cls-2,
.cls-5,
.cls-6,
.cls-7,
.cls-8 {
  stroke-linejoin: round;
}

.cls-3 {
  opacity: 0.5;
}

.cls-4 {
  clip-path: url(#clip-path);
}

.cls-10,
.cls-15,
.cls-19,
.cls-5,
.cls-56,
.cls-57,
.cls-6,
.cls-66,
.cls-7,
.cls-8 {
  stroke: #fff;
}

.cls-5,
.cls-56,
.cls-57 {
  stroke-width: 1.5px;
}

.cls-6 {
  stroke-width: 2px;
}

.cls-10,
.cls-11,
.cls-15,
.cls-19,
.cls-7,
.cls-8 {
  stroke-width: 2.5px;
}

.cls-9 {
  clip-path: url(#clip-path-2);
}

.cls-10,
.cls-19,
.cls-65,
.cls-67 {
  fill: #fff;
}

.cls-10,
.cls-15,
.cls-56,
.cls-57,
.cls-64,
.cls-66,
.cls-68,
.cls-69 {
  stroke-miterlimit: 10;
}

.cls-12 {
  font-size: 63.53px;
  font-family: ArialMT, Arial;
}

.cls-13 {
  clip-path: url(#clip-path-3);
}

.cls-14 {
  clip-path: url(#clip-path-4);
}

.cls-16 {
  clip-path: url(#clip-path-5);
}

.cls-17 {
  clip-path: url(#clip-path-6);
}

.cls-18 {
  stroke-width: 0.71px;
}

.cls-20 {
  clip-path: url(#clip-path-7);
}

.cls-21 {
  clip-path: url(#clip-path-8);
}

.cls-22 {
  clip-path: url(#clip-path-9);
}

.cls-23 {
  letter-spacing: -0.07em;
}

.cls-24 {
  clip-path: url(#clip-path-10);
}

.cls-25 {
  clip-path: url(#clip-path-11);
}

.cls-26 {
  clip-path: url(#clip-path-12);
}

.cls-27 {
  clip-path: url(#clip-path-13);
}

.cls-28 {
  clip-path: url(#clip-path-14);
}

.cls-29 {
  clip-path: url(#clip-path-15);
}

.cls-30 {
  clip-path: url(#clip-path-16);
}

.cls-31 {
  clip-path: url(#clip-path-17);
}

.cls-32 {
  clip-path: url(#clip-path-18);
}

.cls-33 {
  clip-path: url(#clip-path-19);
}

.cls-34 {
  clip-path: url(#clip-path-20);
}

.cls-35 {
  clip-path: url(#clip-path-21);
}

.cls-36 {
  opacity: 0.6;
}

.cls-37 {
  clip-path: url(#clip-path-22);
}

.cls-38 {
  clip-path: url(#clip-path-23);
}

.cls-39 {
  clip-path: url(#clip-path-24);
}

.cls-40 {
  clip-path: url(#clip-path-25);
}

.cls-41 {
  clip-path: url(#clip-path-26);
}

.cls-42 {
  clip-path: url(#clip-path-27);
}

.cls-43 {
  clip-path: url(#clip-path-28);
}

.cls-44 {
  clip-path: url(#clip-path-29);
}

.cls-45 {
  clip-path: url(#clip-path-30);
}

.cls-46 {
  clip-path: url(#clip-path-31);
}

.cls-47 {
  clip-path: url(#clip-path-32);
}

.cls-48 {
  clip-path: url(#clip-path-33);
}

.cls-49 {
  clip-path: url(#clip-path-34);
}

.cls-50 {
  clip-path: url(#clip-path-35);
}

.cls-51 {
  clip-path: url(#clip-path-36);
}

.cls-52 {
  clip-path: url(#clip-path-37);
}

.cls-53 {
  clip-path: url(#clip-path-38);
}

.cls-54 {
  clip-path: url(#clip-path-39);
}

.cls-55 {
  clip-path: url(#clip-path-40);
}

.cls-58 {
  clip-path: url(#clip-path-41);
}

.cls-59 {
  clip-path: url(#clip-path-42);
}

.cls-60 {
  clip-path: url(#clip-path-43);
}

.cls-61 {
  clip-path: url(#clip-path-44);
}

.cls-62 {
  clip-path: url(#clip-path-45);
}

.cls-63 {
  clip-path: url(#clip-path-46);
}

.cls-64 {
  stroke: #d6d6d6;
}

.cls-65,
.cls-70 {
  font-size: 24px;
  margin-top: 2px;
  position: relative;
  display: block;
}

.cls-68 {
  stroke: #c9c9c9;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.cls-69 {
  stroke: #c6c6c6;
}
</style>
