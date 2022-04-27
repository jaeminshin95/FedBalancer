import os

config_lines = [
    'behav_hete False',
    'hard_hete True',
    'no_training False',
    'realworld False',
    'dataset big_reddit',
    'model topk_stacked_lstm',
    'num_rounds 750',
    'max_client_num -1',
    'learning_rate 2',
    'eval_every 5',
    'clients_per_round 100',
    'min_selected 1',
    'max_sample 2147483647',
    'batch_size 10',
    # 'seed 0',
    'round_ddl 60 0',
    'update_frac 0.01',
    'aggregate_algorithm SucFedAvg',
    'num_epochs 5',
    'global_deadline_time 15000',
]


baseline_lines = [
(['fedavg_ddl_fixed_1_0'], ['ddl_baseline_fixed True', 'ddl_baseline_fixed_value_multiplied_at_mean 1.0']),
(['fedavg_ddl_fixed_2_0'], ['ddl_baseline_fixed True', 'ddl_baseline_fixed_value_multiplied_at_mean 2.0']),
(['fedavg_ddl_smartpc'], ['ddl_baseline_smartpc True', 'ddl_baseline_smartpc_percentage 0.8']),
(['fedavg_ddl_waitforall'], ['ddl_baseline_smartpc True', 'ddl_baseline_smartpc_percentage 1.0']),
(['fedprox_mu_0_0_ddl_fixed_1_0'], ['ddl_baseline_fixed True', 'ddl_baseline_fixed_value_multiplied_at_mean 1.0', 'fedprox True']),
(['fedprox_mu_0_0_ddl_fixed_2_0'], ['ddl_baseline_fixed True', 'ddl_baseline_fixed_value_multiplied_at_mean 2.0', 'fedprox True'])
]

process_count = 0
gpu_id = {}
gpu_id[0] = 0
gpu_id[1] = 0
gpu_id[2] = 1
gpu_id[3] = 1
gpu_id[4] = 2
gpu_id[5] = 3
gpu_id[6] = 4
gpu_id[7] = 5
gpu_id[8] = 6
gpu_id[9] = 7
gpu_id[10] = 0
gpu_id[11] = 1


for seed in range(1,3):
    for baseline in baseline_lines:
        new_config_file = open('configs/paper_experiments/211102_baselines/reddit/reddit_'+baseline[0][0]+'_rs'+str(seed)+'.cfg', 'w')
        for line in config_lines:
            new_config_file.write(line+'\n')
        for line in baseline[1]:
            new_config_file.write(line+'\n')
        new_config_file.write('seed '+str(seed)+'\n')
        new_config_file.close()
        os.system('CUDA_VISIBLE_DEVICES='+str(gpu_id[process_count])+' python main.py --config=configs/paper_experiments/211102_baselines/reddit/reddit_'+baseline[0][0]+'_rs'+str(seed)+'.cfg &')
        process_count += 1

# action_steps = [5, 10, 20]
# lr_stepsizes = [0.01, 0.05, 0.1, 0.2, 0.25]
# ddl_stepsizes = [0.01, 0.05, 0.1, 0.2, 0.25]
# fb_ps = [0.0, 0.25]

# process_count = 0

# for action_step in action_steps:
#     for lr_stepsize in lr_stepsizes:
#         for ddl_stepsize in ddl_stepsizes:
#             for fb_p in fb_ps:
#                 str_as = str(action_step)
#                 str_lr = '_'.join(str(lr_stepsize).split('.'))
#                 str_ddl = '_'.join(str(ddl_stepsize).split('.'))
#                 str_fb_p = '_'.join(str(fb_p).split('.'))
#                 new_config_file = open('configs/paper_experiments/210726/har_fb_p'+str_fb_p+'_as'+str_as+'_lss'+str_lr+'_dss'+str_ddl+'.cfg', 'w')
#                 for line in lines:
#                     tmp = line.strip().split(' ')
#                     if 'fedbalancer_action_step' in tmp:
#                         tmp[1] = str(action_step)
#                     elif 'fb_simple_control_lt_stepsize' in tmp:
#                         tmp[1] = str(lr_stepsize)
#                     elif 'fb_simple_control_ddl_stepsize' in tmp:
#                         tmp[1] = str(ddl_stepsize)
#                     elif 'fb_p' in tmp:
#                         tmp[1] = str(fb_p)
#                     new_config_file.write(' '.join(tmp)+'\n')
#                 new_config_file.close()
#                 os.system('CUDA_VISIBLE_DEVICES='+str(7-(process_count//30))+' python main.py --config=configs/paper_experiments/210726/har_fb_p'+str_fb_p+'_as'+str_as+'_lss'+str_lr+'_dss'+str_ddl+'.cfg &')
#                 process_count += 1